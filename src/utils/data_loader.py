import pandas as pd


def load_csv(path):
    """Load dataset from CSV file."""
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None


def preview_data(df):
    """Print dataset preview."""
    if df is not None:
        print("\nDataset Shape:", df.shape)
        print("\nFirst 5 Rows:")
        print(df.head())
    else:
        print("No data to preview.")