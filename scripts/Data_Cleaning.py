
import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_excel(
    "ApexPlanet_DataAnalytics_Dataset.xlsx",
    sheet_name="Sales_Dataset"
)

# Create cleaning copy
clean_df = df.copy()

# Handle missing values
clean_df["Age"] = clean_df["Age"].fillna(
    clean_df["Age"].median()
)

clean_df["City"] = clean_df["City"].fillna("Unknown")

# Standardize date
clean_df["Order_Date"] = pd.to_datetime(
    clean_df["Order_Date"],
    errors="coerce"
)

# Remove unnecessary spaces
for col in clean_df.select_dtypes(include="object").columns:
    clean_df[col] = clean_df[col].str.strip()

# Create unique transaction identifier
clean_df.insert(
    0,
    "Transaction_Row_ID",
    range(1, len(clean_df) + 1)
)

# Flag repeated Order IDs
clean_df["Duplicate_Order_ID_Flag"] = (
    clean_df.duplicated(
        subset=["Order_ID"],
        keep=False
    )
)

# Flag sales outliers
Q1 = clean_df["Total_Sales"].quantile(0.25)
Q3 = clean_df["Total_Sales"].quantile(0.75)
IQR = Q3 - Q1

upper_limit = Q3 + 1.5 * IQR

clean_df["Sales_Outlier_Flag"] = (
    clean_df["Total_Sales"] > upper_limit
)

# Export cleaned dataset
clean_df.to_csv(
    "Cleaned_Sales_Dataset.csv",
    index=False
)

print("Data cleaning completed successfully!")
print("Total records:", len(clean_df))
print("Missing values:", clean_df.isnull().sum().sum())
print("Duplicate rows:", clean_df.duplicated().sum())
