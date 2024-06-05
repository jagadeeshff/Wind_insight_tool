import pandas as pd



df = pd.read_csv('wind.csv')

# Convert the 'Date/Time' column to datetime
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Set 'Date/Time' as the index (optional, but useful for time series data)
df.set_index('Date/Time', inplace=True)

# Interpolate missing values
df['100m_S Avg [m/s]'] = df['100m_S Avg [m/s]'].interpolate(method='linear')

print(df['100m_S Avg [m/s]'])
