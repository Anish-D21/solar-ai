import pandas as pd

# --- CONFIGURABLE ASSUMPTIONS ---
ELECTRICITY_INFLATION = 0.05     # 5% yearly tariff increase
SOLAR_DEGRADATION = 0.005        # 0.5% yearly panel degradation
SIMULATION_YEARS = 10

# Approx installation cost (₹ per kW)
COST_PER_KW = 55000


def estimate_installation_cost(system_size_kw):
    """
    Estimate solar installation cost based on system size.
    """
    return system_size_kw * COST_PER_KW


def simulate_savings(monthly_generation_kwh, tariff, system_size_kw):
    """
    Simulates 10-year solar savings with inflation & degradation.
    Returns:
        yearly_df (DataFrame)
        total_savings
        break_even_year
        installation_cost
    """

    installation_cost = estimate_installation_cost(system_size_kw)

    yearly_data = []
    cumulative_savings = 0
    break_even_year = None

    current_tariff = tariff
    current_generation = monthly_generation_kwh * 12  # convert to yearly

    for year in range(1, SIMULATION_YEARS + 1):

        yearly_savings = current_generation * current_tariff
        cumulative_savings += yearly_savings

        if cumulative_savings >= installation_cost and break_even_year is None:
            break_even_year = year

        yearly_data.append({
            "Year": year,
            "Tariff (₹/kWh)": round(current_tariff, 2),
            "Solar Generation (kWh/year)": round(current_generation, 2),
            "Yearly Savings (₹)": round(yearly_savings, 2),
            "Cumulative Savings (₹)": round(cumulative_savings, 2)
        })

        # Apply next year adjustments
        current_tariff *= (1 + ELECTRICITY_INFLATION)
        current_generation *= (1 - SOLAR_DEGRADATION)

    yearly_df = pd.DataFrame(yearly_data)

    return yearly_df, round(cumulative_savings, 2), break_even_year, installation_cost