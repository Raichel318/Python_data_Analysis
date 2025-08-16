import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# 1. Load data (CSV version)
file_path = '/Users/raichel/Desktop/Hydroelectricdataset.xls'  # Update with your CSV path
df = pd.read_excel(file_path)

# 2. Parameter table (for dynamic start date)
params = {
    'year': 2020,
    'month': 6,
    'day': 29
}

# 3. Convert Week number into Week Start Date
df['WEEKStartDate'] = pd.to_datetime(datetime(params['year'], params['month'], params['day'])) + pd.to_timedelta((df['Week']-1)*7, unit='D')

# 4. Total Other Storage
df['Total_Other_Storage'] = df[['Hawea:End Storage [GWh]', 'Taupo:End Storage [GWh]', 'Pukaki:End Storage [GWh]']].sum(axis=1)
df['Total_Other_Storage'] = df['Total_Other_Storage'].round(2)

# 5. Assign Seasons based on WEEKStartDate
def assign_season(date):
    if date >= datetime(2022,10,3):
        return 'Spring'
    elif date >= datetime(2022,6,27):
        return 'Winter'
    elif date >= datetime(2022,3,28):
        return 'Autum'
    elif date >= datetime(2021,12,27):
        return 'Summer'
    else:
        return 'Unknown'

df['Season'] = df['WEEKStartDate'].apply(assign_season)

# 6. Seasonal Maximum of Other Storage
seasonal_max = df.groupby('Season')['Total_Other_Storage'].transform('max')
df['Seasonal_Max_Other_Storage'] = seasonal_max

# 7. Total Other Storage Percentage
df['Total_Other_Storage_Perc'] = (df['Total_Other_Storage'] / df['Seasonal_Max_Other_Storage']).round(2)

# 8. Other Storage Level
def storage_level(p):
    if p >= 0.8:
        return 'Very High'
    elif p >= 0.6:
        return 'High'
    elif p >= 0.4:
        return 'Medium'
    elif p >= 0.2:
        return 'Low'
    else:
        return 'Very Low'

df['Other_Storage_Level'] = df['Total_Other_Storage_Perc'].apply(storage_level)

# 9. Clean Season column (optional)
df['Season'] = df['Season'].str.strip().str.title()

# 10. Plotting: Tekapo Storage vs Water Value per Season
colors = {
    'Very Low': '#800000',
    'Low': '#FF0000',
    'Medium': '#FFDB58',
    'High': '#87CEEB',
    'Very High': '#000080'
}

sns.set(style="whitegrid")
valid_seasons = ['Summer', 'Autum', 'Winter', 'Spring']

for season in valid_seasons:
    data_season = df[df['Season'] == season]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=data_season,
        x='Tekapo:End Storage [GWh]',
        y='Tekapo:Water Values [$/MWh]',
        hue='Other_Storage_Level',
        palette=colors,
        alpha=0.7
    )
    plt.title(f'Tekapo Water Value vs Storage - {season} 2022')
    plt.xlabel('Tekapo Storage (GWh)')
    plt.ylabel('Water Value ($/MWh)')
    plt.legend(title='Other Storage Level')
    plt.tight_layout()
    
    filename = f'Tekapo_WaterValue_vs_Storage_{season}.png'
    plt.savefig(filename, dpi=300)
    plt.show()

# 11. Save cleaned and calculated dataset
df.to_csv('Cleaned_Hydroelectric_Data.csv', index=False)
