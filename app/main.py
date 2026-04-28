import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, filter_data

st.set_page_config(page_title="Climate Analysis Dashboard", layout="wide")

st.title("🌍 Climate Vulnerability Dashboard")
df = load_data()

# Sidebar: Controls
st.sidebar.header("Filter Settings")
selected_countries = st.sidebar.multiselect("Select Countries", df['Country'].unique(), default=df['Country'].unique())
year_range = st.sidebar.slider("Select Year Range", int(df['YEAR'].min()), int(df['YEAR'].max()), (2015, 2026))
variable = st.sidebar.selectbox("Select Variable to Visualize", ['T2M', 'PRECTOTCORR', 'T2M_MAX'])

# Filter Data
filtered_df = filter_data(df, selected_countries, year_range)

# Dashboard Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{variable} Trend")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=filtered_df, x='YEAR', y=variable, hue='Country', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader(f"{variable} Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=filtered_df, x='Country', y=variable, ax=ax)
    st.pyplot(fig)