import pandas as pd
from pathlib import Path


def get_project_root():
    """
    Returns the root folder of the project dynamically.
    Works regardless of where the script is run from.
    """
    return Path(__file__).resolve().parents[1]


def load_csv(filename):
    """
    Loads a CSV file from the /data directory safely.
    """
    root = get_project_root()
    file_path = root / "data" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found")

    df = pd.read_csv(file_path)
    return df


def preview_data(df):
    print("\nDataset Shape:", df.shape)
    print("\nFirst 5 Rows:\n", df.head())