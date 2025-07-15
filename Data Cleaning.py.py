# Import Libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the raw dataset
df = pd.read_csv('1000-Supermarket-Sales.csv')
# Display the first few rows
print(df.head())

# Basic Exploration

# Overview of the dataset
print(df.info())
# Summary statistics
print(df.describe(include='all'))
# Checking for missing values
print(df.isnull().sum())

#Cleaning Steps

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("\n✅ Column names after cleaning:")
print(df.columns)
# Convert 'time' to datetime objects using the correct format and then extract the time component
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
# Extract the hour from the datetime objects
df['hour'] = pd.to_datetime(df['time'].astype(str), format='%H:%M:%S', errors='coerce').dt.hour
# Print the first few rows to verify the changes
print(df[['time', 'hour']].head())

# Ensure numeric columns are correctly typed
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['total'] = pd.to_numeric(df['total'], errors='coerce')
print(df.dtypes)

for col in ['gender', 'product_line', 'city']:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()
for col in ['gender', 'product_line', 'city']:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()
        print(f"✅ {col} column cleaned.")
    else:
        print(f"❌ {col} column not found in the DataFrame")

       
        # Feature Engineering
        df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.day_name()
df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])

if 'gross_income' in df.columns and 'total' in df.columns:
    df['gross_margin'] = df['gross_income'] / df['total']
    print("✅ 'gross_margin' column added.")
else:
    print("❌ 'gross_income' or 'total' column not found in the DataFrame")

    # Handling Duplicates
    df = df.drop_duplicates()
print(df.shape)

# Save Cleaned Data
print("\n✅ Final cleaned dataset preview:")
print(df.head())
df.to_csv("cleaned_1000_supermarket_sales.csv", index=False)
print("\n💾 Cleaned data saved as 'cleaned_1000_supermarket_sales.csv'.")

# Final check
print(df.info())
print(df.head())

#Visualization
df.groupby('city')['total'].sum().plot(kind='bar', title='Total Sales by City')
plt.ylabel('Sales Amount')
plt.show()

