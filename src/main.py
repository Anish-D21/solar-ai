from utils.data_loader import load_csv, preview_data


def main():
    print("🌞 Solar AI System Starting...")

    df = load_csv("solar_data.csv")
    preview_data(df)


if __name__ == "__main__":
    main()