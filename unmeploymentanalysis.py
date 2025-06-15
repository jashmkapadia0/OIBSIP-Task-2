import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Strip extra spaces in column names
df.columns = df.columns.str.strip()

# Drop missing values
df_clean = df.dropna()

# Convert 'Date' to datetime format
df_clean['Date'] = pd.to_datetime(df_clean['Date'], dayfirst=True)

# Sort by date
df_clean = df_clean.sort_values(by='Date')

# Set seaborn style
sns.set(style="darkgrid")

# Plot
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_clean, x='Date', y='Estimated Unemployment Rate (%)', hue='Region', legend=False)
plt.title('Estimated Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.tight_layout()
plt.show()
