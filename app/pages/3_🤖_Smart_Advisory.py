import streamlit as st

st.set_page_config(page_title="Smart Advisory", page_icon="🤖", layout="wide")

st.title("🤖 Smart System Advisory")

if not st.session_state.get("analyzed"):
    st.warning("Please go to the Home page and run the analysis first.")
    st.stop()

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🛠️ System Health & Faults")
    fault_data = st.session_state.get("fault_data")
    
    if fault_data:
        if fault_data["fault_detected"]:
            st.error(fault_data["message"])
        else:
            st.success(fault_data["message"])
            
        st.write(f"**Deviation percentage:** {fault_data['deviation_percent']}%")
        st.progress(int(fault_data['efficiency_score']))
        st.write(f"**Efficiency score:** {fault_data['efficiency_score']}%")
    else:
        st.info("No 'Actual Production' input was provided on the Home page. Fault Detection Engine is suspended.")

with col2:
    st.subheader("🧠 Operational Intelligence")
    advice_list = st.session_state.get("advice_list", [])
    
    if advice_list:
        for adv in advice_list:
            st.markdown(f"> {adv}")
    else:
        st.write("No specific intelligence generated at this time.")

st.markdown("---")
st.subheader("📡 NASA API Debug Context")
with st.expander("Show AI Feature Data Used for Prediction"):
    st.json(st.session_state.get("solar_info", {}))
