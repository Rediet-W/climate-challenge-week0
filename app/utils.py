import pandas as pd
import os

def load_data():
    """Loads all clean CSVs into a single DataFrame."""
    countries = ['ethiopia', 'kenya', 'sudan', 'tanzania', 'nigeria']
    df_list = []
    # Assumes data is in the ../data/ directory relative to the app folder
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    
    for country in countries:
        path = os.path.join(data_dir, f'{country}_clean.csv')
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['Country'] = country
            df_list.append(df)
            
    return pd.concat(df_list, ignore_index=True)

def filter_data(df, countries, year_range):
    """Filters data based on user selection."""
    return df[
        (df['Country'].isin(countries)) & 
        (df['YEAR'] >= year_range[0]) & 
        (df['YEAR'] <= year_range[1])
    ]