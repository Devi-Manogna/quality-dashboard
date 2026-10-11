
import pandas as pd

LOW_VOLTAGE_LIMIT = 3.3

def clean_data(df):
    """Remove invalid and duplicate records."""
    df = df.dropna(subset=["Cell_ID", "Voltage"])
    df = df.drop_duplicates(subset=["Cell_ID"])
    return df

def find_low_voltage_cells(df):
    """Return cells below the voltage threshold."""
    return df[df["Voltage"] < LOW_VOLTAGE_LIMIT].copy()

def calculate_failure_rate(df):
    """Return the inspection failure rate as a percentage."""
    if df.empty:
        return 0.0

    failed = (df["Inspection_Result"] == "Fail").sum()
    return failed / len(df) * 100
