## Dataset

We used the [Online Retail Dataset](https://www.kaggle.com/datasets/vijayuv/onlineretail) from Kaggle, which contains real-world transactional data of a UK-based online retail store.

Due to GitHub file size limitations, the dataset is not uploaded directly in this repository.

You can download it manually from the link above and place it in the `data/` folder.

Performed by: Mayank Sarkar

Project: Online Retail Dataset Analysis

DATA CLEANING:-

Overview
-This document outlines the data cleaning steps performed on the OnlineRetail.csv dataset to ensure data quality and prepare it for analysis and modeling.

Steps Performed:-
Data Loading

-Loaded the dataset using pandas with ISO-8859-1 encoding to handle special characters.

Initial Inspection

-Used .head(), .info(), and .describe() to understand the structure, data types, and summary statistics.

Handling Missing Values

-Removed rows with missing CustomerID as they are essential for customer-level analysis.

Duplicate Removal

-Checked and dropped duplicate rows to avoid redundancy.

Data Type Conversions

-Converted InvoiceDate column to datetime format for time-based analysis.

Filtering Invalid Entries

-Removed rows with negative or zero Quantity and UnitPrice as they are likely returns or input errors.

Feature Engineering (Optional)

-Created new features such as TotalPrice = Quantity * UnitPrice for RFM and sales analysis.

Scaling (If Required)

-Used StandardScaler for normalizing numerical columns before clustering or modeling.

Tools Used:-
Python (pandas, matplotlib, seaborn, scikit-learn)

