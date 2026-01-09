import pandas as pd
cols = [
    "Date",
    "County",
    "Store Name",
    "Sale (Dollars)"
]

df = pd.read_excel(
    r"C:\Users\flowe\Desktop\Projects\Iowa Liquor Sales\Iowa_Liquor_Sales_20260109.xlsx",
    usecols=cols,
    parse_dates=["Date"],
)

# Convert Sale (Dollars) to numeric
df["Sale (Dollars)"] = pd.to_numeric(df["Sale (Dollars)"].str.replace('$', ''), errors='coerce')

total_sales = df["Sale (Dollars)"].sum()

sales_by_county = (
    df.groupby("County")["Sale (Dollars)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

monthly_sales = (
    df.set_index("Date")
    .resample("M")["Sale (Dollars)"]
    .sum()
)

import matplotlib.pyplot as plt

file_path = r"C:\Users\flowe\Desktop\Projects\Iowa Liquor Sales\Iowa_Liquor_Sales_20260109.xlsx"
df = pd.read_excel(file_path, sheet_name="Iowa_Liquor_Sales_20260109")

# Keep only the columns we need and clean them
df = df[["Date", "County", "Sale (Dollars)"]].copy()
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Sale (Dollars)"] = pd.to_numeric(df["Sale (Dollars)"], errors="coerce")
df = df.dropna(subset=["Date", "County", "Sale (Dollars)"])

# Top 10 counties by total sales
sales_by_county = df.groupby("County")["Sale (Dollars)"].sum().nlargest(10)
sales_by_county_m = sales_by_county / 1_000_000

# Monthly total sales across the whole file
monthly_sales = df.set_index("Date")["Sale (Dollars)"].resample("MS").sum()

ax = sales_by_county_m.plot(kind="bar", title="Top 10 Counties by Total Sales")
ax.bar_label(ax.containers[0], fmt='$%.1fM')
plt.ylabel("Total Sales (Millions)")
plt.savefig("top_counties_sales.png")
plt.show()

monthly_sales.plot(title="Monthly Iowa Liquor Sales Trend")
plt.ylabel("Total Sales (Dollars)")
plt.savefig("monthly_sales_trend.png")
plt.show()
