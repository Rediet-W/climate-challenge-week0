import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # It reads the small summary file directly from the repo
    return pd.read_csv('app/insights.csv')

def filter_data(df, countries, year_range):
    return df[
        (df['Country'].isin(countries)) & 
        (df['YEAR'] >= year_range[0]) & 
        (df['YEAR'] <= year_range[1])
    ]