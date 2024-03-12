import pandas as pd
import numpy as np

csv_file = 'DatasetModed.csv'
df = pd.read_csv(csv_file)

# Normalise ID column
df['ID'] = df['ID'].str.replace('A-', '')

# Normalise datetime columns
df['Start_Time'] = pd.to_datetime(df['Start_Time'].str.replace(r'\.\d+', ''), errors='coerce')
df['End_Time'] = pd.to_datetime(df['End_Time'].str.replace(r'\.\d+', ''), errors='coerce')

# Add new column
df['Duration'] = (df['End_Time'] - df['Start_Time']).dt.total_seconds()
df['Duration'] = df['Duration'].replace([np.inf, -np.inf, np.nan], 0)
df['Duration'] = df['Duration'].astype(int)

# Cut time values
df['Start_Time'] = df['Start_Time'].dt.date

# Drop the column
df.drop(columns=['End_Time'], inplace=True)

df.to_csv(csv_file, index=False)
