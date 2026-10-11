
import pandas as pd

from analysis import (
    clean_data,
    find_low_voltage_cells,
    calculate_failure_rate,
)


def test_low_voltage_cells():
    df = pd.DataFrame({
        "Cell_ID": ["C101", "C102", "C103"],
        "Voltage": [3.5, 3.2, 3.7],
        "Inspection_Result": ["Pass", "Fail", "Pass"],
    })

    result = find_low_voltage_cells(df)

    assert result["Cell_ID"].tolist() == ["C102"]


def test_failure_rate():
    df = pd.DataFrame({
        "Cell_ID": ["C101", "C102"],
        "Voltage": [3.5, 3.2],
        "Inspection_Result": ["Pass", "Fail"],
    })

    assert calculate_failure_rate(df) == 50.0
