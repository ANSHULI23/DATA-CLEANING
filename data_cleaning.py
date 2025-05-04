import pandas as pd

# 1: Load CSV
try:
    data = pd.read_csv('my_data.csv')
except FileNotFoundError:
    print("Error: 'my_data.csv' not found.")
    exit()

# Inspect data
print("\nInitial Data:")
print(data.head())
print("\nColumn Info:")
print(data.info())

# 2: Clean Data

# 2.1: Handle Missing
print("\nMissing Data:")
print(data.isnull().sum())

data = data.dropna()  # Drop rows with any missing

print("\nMissing Handled:")
print(data.isnull().sum())

# 2.2: Remove Duplicates
print("\nDuplicates:")
print(f"Before: {data.duplicated().sum()}")

data = data.drop_duplicates()

print(f"After: {data.duplicated().sum()}")

# 2.3: Fix Data Types
print("\nData Types:")
print(data.dtypes)

# Convert 'Age' to int
if 'Age' in data.columns:
    data['Age'] = pd.to_numeric(data['Age'], errors='coerce').fillna(0).astype(int)
else:
    print("Warning: 'Age' not found.")

# Convert 'Salary' to numeric
if 'Salary' in data.columns:
    data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce').fillna(0)
else:
    print("Warning: 'Salary' not found.")

print("\nData Types Fixed:")
print(data.dtypes)

# 2.4: Rename Columns (Optional)
print("\nRename:")
print("Before:", data.columns)

if 'ID' in data.columns:
    data = data.rename(columns={'ID': 'CustomerID'})
    print("Renamed 'ID'")
else:
    print("Warning: 'ID' not found.")

print("After:", data.columns)

# 2.5: Handle Outliers (Example: 'Salary')
print("\nOutliers:")
if 'Salary' in data.columns:
    data = data[data['Salary'] < 1000000]  # Example threshold
    print("Handled 'Salary'")
else:
    print("Warning: 'Salary' not found.")

# 3: Save Cleaned
data.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved.")

# 4: Display Cleaned
print("\nCleaned Data:")
print(data.head())
print(data.info())