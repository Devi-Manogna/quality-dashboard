
from data_loader import load_data
from analysis import (
    clean_data,
    find_low_voltage_cells,
    calculate_failure_rate,
)


def main():
    df = load_data()
    print("Loaded shape:", df.shape)

    clean_df = clean_data(df)
    print("Cleaned shape:", clean_df.shape)

    low_voltage_df = find_low_voltage_cells(clean_df)
    print("\nLow-voltage cells:")
    print(low_voltage_df)

    failure_rate = calculate_failure_rate(clean_df)
    print(f"\nInspection failure rate: {failure_rate:.2f}%")


if __name__ == "__main__":
    main()
