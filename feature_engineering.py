import pandas as pd

# =========================================
# Load Clean Dataset
# =========================================

df = pd.read_csv("books_raw.csv")

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# =========================================
# Feature 1 : Book Age
# =========================================

CURRENT_YEAR = 2025

df["Book Age"] = CURRENT_YEAR - df["Publish Year"]

print("\n✓ Book Age Created")

# =========================================
# Feature 2 : Publication Decade
# =========================================

df["Publication Decade"] = (df["Publish Year"] // 10) * 10

print("✓ Publication Decade Created")

# =========================================
# Feature 3 : Edition Category
# =========================================

def edition_category(x):
    if x <= 100:
        return "Low"
    elif x <= 500:
        return "Medium"
    else:
        return "High"

df["Edition Category"] = df["Edition Count"].apply(edition_category)

print("✓ Edition Category Created")

# =========================================
# Display New Dataset
# =========================================

print("\nFirst 10 Rows\n")

print(df.head(10))

# =========================================
# Save Dataset
# =========================================

df.to_csv("books_feature_engineered.csv", index=False)

print("\nDataset saved successfully as books_feature_engineered.csv")

print("\nDataset Shape")

print(df.shape)

print("\nColumns")

print(df.columns)