import os
from utils.data_loader import load_csv, preview_data


def main():
    print("🌞 Solar AI System Starting...\n")

    # Temporary dataset path (we'll add real data later)
    data_path = os.path.join("data", "solar_data.csv")

    if not os.path.exists(data_path):
        print("⚠ Dataset not found yet. We'll add it in the next step.")
        return

    df = load_csv(data_path)
    preview_data(df)


if __name__ == "__main__":
    main()