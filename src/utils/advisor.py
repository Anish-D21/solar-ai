def generate_advisory(generation, monthly_usage, break_even_year, fault_data=None):
    """
    Generates smart, rule-based recommendations for the solar user.
    
    Args:
        generation (float): Monthly expected solar generation (kWh).
        monthly_usage (float): User's monthly grid consumption (kWh).
        break_even_year (int): Year at which investment pays off.
        fault_data (dict): From detect_fault module (optional).
        
    Returns:
        list[str]: A list of advisory messages.
    """
    advice = []
    
    # Usage vs Production rules
    if generation > monthly_usage * 0.8:
        advice.append("💡 **High Production:** Your system covers a huge portion of your usage. Consider running heavy appliances (AC, washing machine) during peak daylight (11 AM - 3 PM) to maximize self-consumption instead of exporting to the grid.")
    elif generation < monthly_usage * 0.4:
        advice.append("🔋 **Low Coverage:** Your solar system covers less than half your usage. Consider upgrading into a higher capacity down the line or investing in energy-efficient appliances.")

    # Financial / Investment advice
    if break_even_year is not None:
        if break_even_year <= 5:
            advice.append(f"📈 **Excellent Investment:** A Break-even under 5 years is phenomenal. Going solar here yields high financial returns.")
        elif break_even_year <= 8:
            advice.append(f"📊 **Solid Returns:** Breaking even in {break_even_year} years is well within the industry standard (5-8 years).")
        else:
            advice.append(f"⚖️ **Long Term Payback:** Expected break-even is {break_even_year} years. Consider checking local state subsidies to reduce initial costs!")

    # Maintenance advice
    if fault_data and fault_data.get("fault_detected"):
        advice.append("🛠️ **Maintenance Warning:** The system seems to be underperforming significantly compared to ML expectations. We strongly advise scheduling a panel cleaning and checking inverter wiring.")
    elif fault_data and fault_data.get("efficiency_score", 0) > 95:
         advice.append("✨ **Peak Efficiency:** Your system is operating at near-perfect efficiency!")

    return advice
