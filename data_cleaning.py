import pandas as pd

# Load dataset
df = pd.read_csv("books_raw.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)
print(df.info())

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())    
