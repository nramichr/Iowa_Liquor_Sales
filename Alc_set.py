import pandas as pd
cols = [
    "Date",
    "County",
    "Store Name",
    "Sale (Dollars)"
]

df = pd.read_csv(
    r"c:\Users\flowe\Desktop\Projects\Iowa Liquor Sales\Iowa_Liquor_Sales_20260102.csv",
    usecols=cols,
    parse_dates=["Date"],
    nrows=500_000
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

sales_by_county.plot(kind="bar", title="Top 10 Counties by Total Sales")
plt.ylabel("Total Sales (Dollars)")
plt.savefig("top_counties_sales.png")
plt.show()

monthly_sales.plot(title="Monthly Iowa Liquor Sales Trend")
plt.ylabel("Total Sales (Dollars)")
plt.savefig("monthly_sales_trend.png")
plt.show()