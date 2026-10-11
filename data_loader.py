
from pathlib import Path
import pandas as pd

DATA_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "battery_cells.csv"
)


def load_data():
    """Load the battery cell dataset."""
    return pd.read_csv(DATA_FILE)
