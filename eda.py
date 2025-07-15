# Exploratory Data Analysis
#Performed By Prabhav Goel
## 1. Top 5 Countries by Number of Transactions

#We analyze the distribution of orders across different countries. This helps us identify where most customers are located, which is useful for geographical segmentation or international strategy.
#Only the top 5 countries with the highest number of transactions are displayed.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Import seaborn
from sklearn.preprocessing import StandardScaler # Import StandardScaler
df = pd.read_csv('OnlineRetail_cleaned.csv', encoding='ISO-8859-1')
df.head(5)
# 1. Top 5 countries by number of transactions
print("Top 5 countries with most orders:")
print(df['Country'].value_counts().head(5))

## 2. Total Revenue by Country (Excluding UK)
#Here, we calculate the total revenue contributed by each country and visualize the top 10 international markets (excluding the United Kingdom, which dominates the dataset).
#This helps identify the most valuable international customer segments for possible expansion.

country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
country_revenue.drop('United Kingdom', errors='ignore').head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Countries by Revenue (excluding UK)")
plt.xlabel("Country")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.show()

## 3. Most Sold Products
#We display the top 10 most frequently sold products by description. This helps understand product demand and may inform clustering features if we consider product preferences.
#Although not directly used in K-Means, it helps in profiling and recommendation strategies.

print("\nTop 10 most sold products:")
print(df['Description'].value_counts().head(10))

## 4. Monthly Revenue Trend
#We group the data by invoice month to observe the revenue trend over time.
#This helps identify seasonality or sales cycles which are crucial for understanding *recency and frequency* — useful for RFM segmentation and marketing timing.

# Make sure InvoiceDate is datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Create InvoiceMonth from InvoiceDate
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')

# Now group by InvoiceMonth
monthly_revenue = df.groupby('InvoiceMonth')['TotalPrice'].sum()

# Plot the trend
plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind='line', marker='o', color='green')
plt.title("Monthly Revenue Over Time")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

## 5. Distribution of Order Values (Below ₹100)
#We visualize the distribution of order values, focusing on small transactions below ₹100.
#This helps detect common purchase sizes, outliers, and customer price sensitivity — which supports monetary-based segmentation.

filtered_df = df[df['TotalPrice'] < 100]
plt.figure(figsize=(10, 5))
plt.hist(filtered_df['TotalPrice'], bins=50, color='skyblue', edgecolor='black')
plt.title("Distribution of Order Values (Below ₹100)")
plt.xlabel("Order Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
print(df[['InvoiceDate', 'InvoiceMonth']].head())
