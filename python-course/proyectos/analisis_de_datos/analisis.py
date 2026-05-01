# ============================================================
# Project 03 — Basic Data Analysis with pandas
# ============================================================
# Analyzes a sample sales dataset:
# - Total and average sales
# - Best and worst performing products
# - Sales by category
# Run: pip install pandas

import pandas as pd

def load_data():
    data = {
        "Product":  ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones",
                     "Webcam", "USB Hub", "Laptop", "Mouse", "Monitor"],
        "Category": ["Computer", "Accessory", "Accessory", "Computer", "Accessory",
                     "Accessory", "Accessory", "Computer", "Accessory", "Computer"],
        "Units":    [5, 30, 20, 8, 15, 12, 25, 3, 45, 6],
        "Price":    [999.99, 29.99, 79.99, 349.99, 89.99, 69.99, 24.99, 999.99, 29.99, 349.99],
        "Month":    ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Mar", "Mar", "Mar", "Mar"]
    }
    df = pd.DataFrame(data)
    df["Total"] = df["Units"] * df["Price"]
    return df

def analyze(df):
    print("=" * 50)
    print("       📊 Sales Analysis Report")
    print("=" * 50)

    print(f"\n📋 Dataset Preview:\n{df.to_string(index=False)}")

    print("\n" + "=" * 50)
    print("  GENERAL STATS")
    print("=" * 50)
    total_revenue = df["Total"].sum()
    total_units = df["Units"].sum()
    avg_price = df["Price"].mean()
    print(f"Total Revenue:   ${total_revenue:,.2f}")
    print(f"Total Units Sold: {total_units}")
    print(f"Average Price:   ${avg_price:.2f}")

    print("\n" + "=" * 50)
    print("  SALES BY CATEGORY")
    print("=" * 50)
    by_category = df.groupby("Category").agg(
        Total_Revenue=("Total", "sum"),
        Units_Sold=("Units", "sum")
    ).sort_values("Total_Revenue", ascending=False)
    print(by_category.to_string())

    print("\n" + "=" * 50)
    print("  SALES BY MONTH")
    print("=" * 50)
    by_month = df.groupby("Month")["Total"].sum().reindex(["Jan", "Feb", "Mar"])
    for month, revenue in by_month.items():
        bar = "█" * int(revenue / 1000)
        print(f"{month}: ${revenue:>10,.2f}  {bar}")

    print("\n" + "=" * 50)
    print("  TOP 3 PRODUCTS BY REVENUE")
    print("=" * 50)
    top = df.groupby("Product")["Total"].sum().sort_values(ascending=False).head(3)
    for i, (product, revenue) in enumerate(top.items(), 1):
        print(f"{i}. {product:<15} ${revenue:,.2f}")

    print("\n" + "=" * 50)
    print("  MOST UNITS SOLD")
    print("=" * 50)
    most_units = df.groupby("Product")["Units"].sum().sort_values(ascending=False).head(3)
    for product, units in most_units.items():
        print(f"{product:<15} {units} units")

def main():
    df = load_data()
    analyze(df)

if __name__ == "__main__":
    main()
