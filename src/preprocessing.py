import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load CSV data file."""
    return pd.read_csv(path)

