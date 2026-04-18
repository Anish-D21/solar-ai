import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Financial Analysis", page_icon="💰", layout="wide")

st.title("💰 Detailed Financial Analysis")

if not st.session_state.get("analyzed"):
    st.warning("Please go to the Home page and run the analysis first.")
    st.stop()

# Get data from session
install_cost = st.session_state["install_cost"]
total_savings = st.session_state["total_savings"]
break_even = st.session_state["break_even"]
yearly_df = st.session_state["yearly_df"]

st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Installation Cost", f"₹{install_cost:,.0f}")
col2.metric("Break-Even Horizon", f"{break_even} Years")
col3.metric("10-Yr Total Savings", f"₹{total_savings:,.0f}")

st.markdown("---")
st.subheader("📈 Return on Investment (ROI) Chart")
st.markdown("A clearer view of your savings over time compared to your initial investment.")

# Custom Plotly Graph (Less confusing)
fig = go.Figure()

# Add Cumulative Savings Line
fig.add_trace(go.Scatter(
    x=yearly_df["Year"],
    y=yearly_df["Cumulative Savings (₹)"],
    mode='lines+markers',
    name='Cumulative Savings',
    line=dict(color='green', width=3)
))

# Add Installation Cost Line
fig.add_trace(go.Scatter(
    x=yearly_df["Year"],
    y=[install_cost] * len(yearly_df),
    mode='lines',
    name='Initial Investment Cost',
    line=dict(color='red', width=2, dash='dash')
))

fig.update_layout(
    xaxis_title="Years",
    yaxis_title="Amount (₹)",
    hovermode="x unified",
    template="plotly_white",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("📊 Year-by-Year Cash Journey")
st.markdown("Dive into the raw numbers below to see strictly what you save each year as tariffs inflate.")
st.dataframe(yearly_df.style.format({
    "Tariff (₹/kWh)": "₹{:.2f}",
    "Solar Generation (kWh/year)": "{:,.2f}",
    "Yearly Savings (₹)": "₹{:,.2f}",
    "Cumulative Savings (₹)": "₹{:,.2f}"
}), use_container_width=True, hide_index=True)

