import pandas as pd

# Load feature engineered dataset
df = pd.read_csv("books_feature_engineered.csv")

print("="*60)
print("CLASS DISTRIBUTION")
print("="*60)

print(df["Edition Category"].value_counts())

print("\nPercentage Distribution")

print((df["Edition Category"].value_counts(normalize=True)*100).round(2))