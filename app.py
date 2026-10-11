
import streamlit as st
import plotly.express as px

from data_loader import load_data
from analysis import (
    clean_data,
    find_low_voltage_cells,
    calculate_failure_rate,
)

st.set_page_config(
    page_title="Battery Quality Dashboard",
    page_icon="🔋",
    layout="wide",
)

st.title("🔋 Battery Quality Dashboard")
st.write("Explore fictional battery manufacturing quality data.")

# Load and prepare the data
df = clean_data(load_data())

# Sidebar filters
st.sidebar.header("Filters")

supplier_options = sorted(df["Supplier_Lot"].unique())

selected_suppliers = st.sidebar.multiselect(
    "Select supplier lots",
    options=supplier_options,
    default=supplier_options,
)

filtered_df = df[
    df["Supplier_Lot"].isin(selected_suppliers)
].copy()

# KPI metrics
low_voltage_df = find_low_voltage_cells(filtered_df)
failure_rate = calculate_failure_rate(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Cells", len(filtered_df))
col2.metric("Low Voltage Cells", len(low_voltage_df))
col3.metric("Inspection Failure Rate", f"{failure_rate:.1f}%")

# Data table
st.subheader("Battery Cell Records")
st.dataframe(filtered_df, use_container_width=True)

# Chart
st.subheader("Voltage by Supplier Lot")

fig = px.box(
    filtered_df,
    x="Supplier_Lot",
    y="Voltage",
    title="Distribution of Cell Voltage",
)

st.plotly_chart(fig, use_container_width=True)

# Low voltage results
st.subheader("Low Voltage Cells")
st.dataframe(low_voltage_df, use_container_width=True)


min_voltage = st.sidebar.slider(
    "Minimum voltage",
    min_value=2.5,
    max_value=4.5,
    value=2.5,
    step=0.05,
)

filtered_df = filtered_df[
    filtered_df["Voltage"] >= min_voltage
].copy()