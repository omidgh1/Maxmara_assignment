import streamlit as st
import pandas as pd


# Load data
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)


# Preload datasets
st.title("Max Mara Product Analysis")

# File paths
file_paths = {
    "Max Mara": "maxmara_cleaned.csv",
    "Net-A-Porter": "netaporter_cleaned.csv",
    "Luisa Via Roma": "luisaviaroma_cleaned.csv"
}

# Load datasets
dfs = {name: load_data(path) for name, path in file_paths.items()}
st.sidebar.success(f"Loaded {len(dfs)} datasets.")

# Display dataset selection
dataset_name = st.sidebar.selectbox("Select a dataset to view", list(dfs.keys()))
selected_df = dfs[dataset_name]

# Display raw data
st.header(f"Dataset: {dataset_name}")
st.write("### Preview")
#st.dataframe(selected_df.head())

# Basic statistics
st.write("### Basic Statistics")
st.write(selected_df.describe(include='all'))

# Analysis options
st.header("Analysis")
analysis_option = st.selectbox(
    "Choose an analysis option:",
    [
        "Summary of Product Availability and Pricing",
        "Identify Most Popular Colors",
        "Discount Analysis",
        "Size Availability Analysis"
    ]
)

# Analysis logic
if analysis_option == "Summary of Product Availability and Pricing":
    st.subheader("Product Availability and Pricing")
    price_summary = selected_df[['current_price', 'previous_price', 'discounted']].describe()
    st.write(price_summary)

elif analysis_option == "Identify Most Popular Colors":
    st.subheader("Most Popular Colors")
    color_counts = selected_df['color'].value_counts()
    st.bar_chart(color_counts)

elif analysis_option == "Discount Analysis":
    st.subheader("Discount Analysis")
    discounted_items = selected_df[selected_df['discounted']]
    discount_rate = discounted_items.shape[0] / selected_df.shape[0] * 100
    st.write(f"Percentage of discounted products: {discount_rate:.2f}%")

elif analysis_option == "Size Availability Analysis":
    st.subheader("Size Availability")
    size_data = selected_df['available_sizes'].value_counts()
    st.bar_chart(size_data)
