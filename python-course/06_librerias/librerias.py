# ============================================================
# Module 06 — Libraries: numpy & pandas
# ============================================================
# Run: pip install numpy pandas

import numpy as np
import pandas as pd

# ============================================================
# NUMPY
# ============================================================
print("=== NUMPY ===")

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Type:", type(arr))

# Math operations (applied to every element)
print("\nArray * 2:", arr * 2)
print("Array ** 2:", arr ** 2)
print("Array + 10:", arr + 10)

# Statistics
data = np.array([15, 22, 8, 34, 19, 27, 11])
print(f"\nData: {data}")
print(f"Mean: {np.mean(data):.2f}")
print(f"Median: {np.median(data):.2f}")
print(f"Std Dev: {np.std(data):.2f}")
print(f"Min: {np.min(data)}, Max: {np.max(data)}")

# 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"\nMatrix shape: {matrix.shape}")
print(f"Matrix:\n{matrix}")

# Range of values
x = np.linspace(0, 10, 5)  # 5 evenly spaced values from 0 to 10
print(f"\nLinspace: {x}")


# ============================================================
# PANDAS
# ============================================================
print("\n=== PANDAS ===")

# Create a DataFrame (like a table / spreadsheet)
data = {
    "Name":   ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age":    [24, 30, 22, 28, 35],
    "City":   ["New York", "London", "Paris", "Berlin", "Tokyo"],
    "Salary": [55000, 72000, 48000, 65000, 90000]
}

df = pd.DataFrame(data)
print(df)

# Basic info
print(f"\nShape: {df.shape}")
print(f"\nColumn types:\n{df.dtypes}")

# Statistics summary
print(f"\nSummary:\n{df.describe()}")

# Access a column
print(f"\nAll names:\n{df['Name'].tolist()}")

# Filter rows
high_earners = df[df["Salary"] > 60000]
print(f"\nEarning more than $60k:\n{high_earners}")

# Add a new column
df["Seniority"] = df["Age"].apply(lambda x: "Senior" if x >= 30 else "Junior")
print(f"\nWith seniority column:\n{df}")

# Sort by salary
df_sorted = df.sort_values("Salary", ascending=False)
print(f"\nSorted by salary:\n{df_sorted[['Name', 'Salary']]}")

# Group by
avg_salary_by_seniority = df.groupby("Seniority")["Salary"].mean()
print(f"\nAverage salary by seniority:\n{avg_salary_by_seniority}")
