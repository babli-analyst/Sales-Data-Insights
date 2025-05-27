# Sales Data Insights

# 1. Import Libraries
import csv
import pandas as pd
import numpy as np

# 2. Load Dataset
file_name = "dataset - Sheet1.csv"
with open(file_name, 'r') as file:
    content = csv.reader(file)
    data = list(content)

df = pd.DataFrame(data[1:], columns=data[0])

# 3. Inspect Data
print("Shape:", df.shape)
print(df.info())

# 4. Clean Data
df.replace('', pd.NA, inplace=True)
df['CustomerName'] = df['CustomerName'].fillna('Unknown')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce').fillna(0)
df['TotalSales'] = pd.to_numeric(df['TotalSales'], errors='coerce').fillna(0)

# 5. Basic Analysis
print("\nSum of Sales by Region:")
print(df.groupby('Region')['TotalSales'].sum())

print("\nAverage Sales per Product:")
print(df.groupby('Product')['TotalSales'].mean())

print("\nHighest Selling Product:")
print(df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(1))

print("\nLowest Selling Product:")
print(df.groupby('Product')['TotalSales'].sum().sort_values(ascending=True).head(1))

# 6. NumPy Stats
print("\n NumPy Statistics:")
numeric_columns = df.select_dtypes(include='number').columns

for col in numeric_columns:
    mean_val = np.mean(df[col])
    median_val = np.median(df[col])
    std_val = np.std(df[col])
    print(f"{col} -> Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std Dev: {std_val:.2f}")
