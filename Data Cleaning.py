# prompt: Collect and clean OnlineRetail dataset.
# Performed by- Mayank Sarkar

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Import seaborn
from sklearn.preprocessing import StandardScaler # Import StandardScaler

df = pd.read_csv('OnlineRetail.csv', encoding='ISO-8859-1')

# Inspect the data
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values
# Drop rows with missing CustomerID - crucial for RFM analysis later
df.dropna(subset=['CustomerID'], inplace=True)
# Fill missing Description values
df['Description'].fillna('Unknown', inplace=True)

# Remove rows with negative Quantity or UnitPrice
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert data types
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype(int)

# Create TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


