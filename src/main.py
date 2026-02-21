from src.data_fetcher import get_city_solar_info
from src.utils.predictor import predict_generation
from src.utils.recommendation import recommend_system_size
from src.utils.finance import simulate_savings
from src.utils.tariff_engine import calculate_slab_bill
from src.utils.geocoder import get_state_from_city


def main():
    print("🌞 Solar AI Advisor\n")

    city = input("Enter your city: ")
    monthly_usage = float(input("Monthly electricity usage (kWh): "))
    roof_area = float(input("Available roof area (sq ft): "))

    # Fetch environmental data
    solar_info = get_city_solar_info(city)
    sun_hours = solar_info["peak_sun_hours"]
    temperature = solar_info["avg_temperature"]

    # Recommend system size
    system_size = recommend_system_size(monthly_usage, roof_area)

    # Predict solar generation
    generation = predict_generation(
        sun_hours,
        roof_area,
        system_size,
        temperature
    )

    print("\n📊 Results:")
    print(f"City: {city}")
    print(f"Peak Sun Hours: {sun_hours}")
    print(f"Recommended System Size: {system_size} kW")
    print(f"Estimated Monthly Solar Generation: {generation:.2f} kWh")

    # --------------------------------------------------
    # Ask user if they know their electricity tariff
    # --------------------------------------------------
    know_tariff = input("\nDo you know your electricity tariff (₹/kWh)? (y/n): ").strip().lower()

    if know_tariff == "y":
        # User provides tariff manually (most accurate)
        effective_tariff = float(input("Enter your tariff (₹/kWh): "))
        print(f"\nUsing user-provided tariff: ₹{effective_tariff:.2f}/kWh")

    else:
        # Auto-detect state from city
        print("\n🔎 Detecting state from city...")
        state = get_state_from_city(city)

        if state:
            print(f"Detected State: {state}")
            original_bill = calculate_slab_bill(monthly_usage, state)

            if original_bill is not None:
                # Convert slab bill → effective ₹/kWh
                effective_tariff = original_bill / monthly_usage
            else:
                print("⚠️ Tariff data not available for this state. Using fallback ₹6/kWh.")
                effective_tariff = 6

        else:
            print("⚠️ Could not detect state. Using fallback ₹6/kWh.")
            effective_tariff = 6

    print(f"\nEffective Electricity Tariff: ₹{effective_tariff:.2f}/kWh")

    # --------------------------------------------------
    # Financial Simulation (10-year ROI)
    # --------------------------------------------------
    yearly_df, total_savings, break_even, install_cost = simulate_savings(
        generation,          # monthly solar generation (kWh)
        effective_tariff,    # ₹ per kWh
        system_size          # system size (kW)
    )

    print("\n💰 Financial Analysis:")
    print(f"Estimated Installation Cost: ₹{install_cost:,.0f}")
    print(f"Break-even Year: {break_even}")
    print(f"10-Year Total Savings: ₹{total_savings:,.0f}")

    print("\n📈 Yearly Projection:")
    print(yearly_df)


if __name__ == "__main__":
    main()