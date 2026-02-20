import pandas as pd
from pathlib import Path


DATA_PATH = Path("data")


def load_csv(filename: str) -> pd.DataFrame:
    """
    Loads a CSV file from the data folder.

    Example:
        df = load_csv("solar_projects.csv")
    """
    file_path = DATA_PATH / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found in /data folder")

    df = pd.read_csv(file_path)
    return df


def preview_data(df: pd.DataFrame, rows: int = 5):
    """Prints a quick preview for debugging."""
    print("\n🔍 Data Preview:")
    print(df.head(rows))
    print("\n📊 Shape:", df.shape)