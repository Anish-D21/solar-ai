import pandas as pd
import os


DATA_PATH = os.path.join("data", "state_tariffs.csv")


def load_tariff_data():
    """Load tariff CSV"""
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError("Tariff file not found at data/state_tariffs.csv")

    df = pd.read_csv(DATA_PATH)
    return df


def get_state_tariffs(state, consumer_type="residential"):
    """Filter tariffs for a given state + consumer type"""
    df = load_tariff_data()

    state_df = df[
        (df["state"].str.lower() == state.lower()) &
        (df["consumer_type"].str.lower() == consumer_type.lower())
    ]

    if state_df.empty:
        return None

    return state_df.sort_values(by="slab_start")


def calculate_slab_bill(units, state, consumer_type="residential"):
    """
    Calculate electricity bill using slab-based billing.
    Returns total cost (₹)
    """

    tariffs = get_state_tariffs(state, consumer_type)

    # Fallback if state not found
    if tariffs is None:
        return None

    remaining_units = units
    total_cost = 0

    for _, row in tariffs.iterrows():
        slab_start = row["slab_start"]
        slab_end = row["slab_end"]
        rate = row["rate"]

        if remaining_units <= 0:
            break

        slab_range = slab_end - slab_start + 1
        units_in_slab = min(remaining_units, slab_range)

        total_cost += units_in_slab * rate
        remaining_units -= units_in_slab

    return round(total_cost, 2)