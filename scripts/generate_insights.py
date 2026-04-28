import pandas as pd
import os

# 1. Load your local raw data
countries = ['ethiopia', 'kenya', 'sudan', 'tanzania', 'nigeria']
df_list = []
for country in countries:
    df = pd.read_csv(f'data/{country}_clean.csv')
    df['Country'] = country
    df_list.append(df)
master_df = pd.concat(df_list, ignore_index=True)

# 2. Aggregate the data (Create the "Insights")
# We group by Year and Country to get annual trends
insights = master_df.groupby(['YEAR', 'Country']).agg({
    'T2M': 'mean',
    'PRECTOTCORR': 'mean',
    'T2M_MAX': lambda x: (x > 35).sum() # Count extreme heat days
}).reset_index()

# 3. Save the tiny summary file
insights.to_csv('app/insights.csv', index=False)
print("Insights generated! 'app/insights.csv' is ready to be committed.")