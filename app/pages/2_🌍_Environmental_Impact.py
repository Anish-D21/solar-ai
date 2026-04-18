import streamlit as st

st.set_page_config(page_title="Environmental Impact", page_icon="🌍", layout="wide")

st.title("🌍 Lifetime Environmental Impact")

if not st.session_state.get("analyzed"):
    st.warning("Please go to the Home page and run the analysis first.")
    st.stop()

env = st.session_state["env_impact"]

st.markdown(f"By going solar, over a **10-year lifespan**, your {st.session_state['system_size']} kW system will produce approximately **{env['lifetime_generation_kwh']:,.0f} kWh** of clean energy.")
st.markdown("Here is how that translates to repairing the Earth:")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("☁️ CO2 Emissions Avoided")
    st.metric("", f"{env['co2_avoided_tons']} Tons", delta="Carbon Negative", delta_color="normal")

with col2:
    st.info("🌳 Trees Planted Equivalent")
    st.metric("", f"{env['trees_planted']} Trees")

with col3:
    st.warning("🚗 Car Miles Avoided")
    st.metric("", f"{env['car_miles_avoided']:,.0f} Miles")

st.markdown("---")
st.markdown("**Did you know?**")
st.info("The average passenger vehicle emits about 400 grams of CO2 per mile. By switching to renewable solar energy, you offset the equivalent of driving cross-country multiple times over!")
