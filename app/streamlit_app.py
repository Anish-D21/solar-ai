import streamlit as st
import os
import sys

# Ensure src modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_fetcher import get_city_solar_info
from src.utils.predictor import predict_generation
from src.utils.recommendation import recommend_system_size
from src.utils.geocoder import get_state_from_city
from src.utils.tariff_engine import calculate_slab_bill
from src.utils.finance import simulate_savings
from src.utils.fault import detect_fault
from src.utils.advisor import generate_advisory
from src.utils.environmental import calculate_environmental_impact

st.set_page_config(page_title="SolarIQ Home", page_icon="⚡", layout="wide")

st.title("⚡ SolarIQ: AI-Based Solar Intelligence")
st.markdown("Welcome to the **SolarIQ Command Center**. Enter your details below to run an AI-powered analysis on your property's solar potential, then navigate to the other pages in the sidebar to explore detailed Financials, Environmental Impact, and Smart Advisories!")

st.markdown("---")

# Initialize session state variables if they don't exist
if "analyzed" not in st.session_state:
    st.session_state["analyzed"] = False

# --- INPUT FORM ---
st.subheader("1. Property Details")
col1, col2, col3 = st.columns(3)
with col1:
    city = st.text_input("City", value=st.session_state.get("city", "Mumbai"))
with col2:
    monthly_usage = st.number_input("Monthly Electricity Usage (kWh)", min_value=50, max_value=10000, value=st.session_state.get("monthly_usage", 300))
with col3:
    roof_area = st.number_input("Available Roof Area (sq ft)", min_value=50.0, value=st.session_state.get("roof_area", 500.0))

st.subheader("2. Advanced (Optional)")
col4, col5 = st.columns(2)
with col4:
    actual_production = st.number_input("Current Actual Monthly Production (kWh)", value=st.session_state.get("actual_production", 0.0), help="For fault detection if you already have solar panels.")
with col5:
    custom_tariff = st.number_input("Custom Tariff (₹/kWh) (Optional)", value=st.session_state.get("custom_tariff", 0.0), help="Leave 0 to auto-detect tariff based on city/state.")

if st.button("🚀 Analyze Solar Potential", use_container_width=True):
    if not city.strip():
        st.error("Please enter a valid city!")
    else:
        with st.spinner("Fetching geolocation and NASA solar data..."):
            try:
                solar_info = get_city_solar_info(city)
                sun_hours = solar_info["peak_sun_hours"]
                temperature = solar_info["avg_temperature"]
                state = get_state_from_city(city)
            except Exception as e:
                st.error(f"Error fetching data for city '{city}'. {str(e)}")
                st.stop()
        
        with st.spinner("Running AI Models & Financial Simulation..."):
            # 2. System Size
            system_size = recommend_system_size(monthly_usage, roof_area)
            
            # 3. AI Prediction
            generation = predict_generation(sun_hours, roof_area, system_size, temperature)

            # 4. Tariff Handling
            if custom_tariff > 0:
                effective_tariff = custom_tariff
                tariff_source = "User Provided"
            else:
                if state:
                    original_bill = calculate_slab_bill(monthly_usage, state)
                    if original_bill is not None:
                        effective_tariff = original_bill / monthly_usage
                        tariff_source = f"Calculated ({state} Slabs)"
                    else:
                        effective_tariff = 6.0
                        tariff_source = "Fallback (₹6.0/kWh)"
                else:
                    effective_tariff = 6.0
                    tariff_source = "Fallback (₹6.0/kWh)"

            # 5. Financial Simulation
            yearly_df, total_savings, break_even, install_cost = simulate_savings(
                generation, effective_tariff, system_size
            )

            # 6. Fault Detection
            fault_data = None
            if actual_production > 0:
                fault_data = detect_fault(generation, actual_production)

            # 7. AI Advisory
            advice_list = generate_advisory(generation, monthly_usage, break_even, fault_data)
            
            # 8. Environmental
            env_impact = calculate_environmental_impact(generation * 12)

        # Store everything in session state
        st.session_state["analyzed"] = True
        st.session_state["city"] = city
        st.session_state["monthly_usage"] = monthly_usage
        st.session_state["roof_area"] = roof_area
        st.session_state["actual_production"] = actual_production
        st.session_state["custom_tariff"] = custom_tariff
        
        # Results
        st.session_state["system_size"] = system_size
        st.session_state["generation"] = generation
        st.session_state["effective_tariff"] = effective_tariff
        st.session_state["tariff_source"] = tariff_source
        st.session_state["yearly_df"] = yearly_df
        st.session_state["total_savings"] = total_savings
        st.session_state["break_even"] = break_even
        st.session_state["install_cost"] = install_cost
        st.session_state["fault_data"] = fault_data
        st.session_state["advice_list"] = advice_list
        st.session_state["env_impact"] = env_impact
        st.session_state["solar_info"] = solar_info

# --- DISPLAY TOP LEVEL RESULTS ---
if st.session_state.get("analyzed"):
    st.success("✅ Analysis Complete! You can now explore the detailed pages in the sidebar.")
    st.markdown("### Top Level Snapshot")
    colA, colB, colC = st.columns(3)
    colA.metric("Recommended System Size", f"{st.session_state['system_size']} kW")
    colB.metric("Predicted Solar Generation", f"{st.session_state['generation']:.1f} kWh / mo")
    colC.metric("Effective Electricity Rate", f"₹{st.session_state['effective_tariff']:.2f} / kWh")
    
    st.info("👈 **Use the left sidebar to dive deep into Financials, Environmental impact, and Smart Insights.**")
