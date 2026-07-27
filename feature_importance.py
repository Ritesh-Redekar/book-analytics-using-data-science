import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("books_feature_engineered.csv")

# Encode categorical columns
author_encoder = LabelEncoder()
subject_encoder = LabelEncoder()
target_encoder = LabelEncoder()

df["Author"] = author_encoder.fit_transform(df["Author"])
df["Subject"] = subject_encoder.fit_transform(df["Subject"])
df["Edition Category"] = target_encoder.fit_transform(df["Edition Category"])

# Features and Target
X = df[
    [
        "Author",
        "Publish Year",
        "Edition Count",
        "Subject",
        "Book Age",
        "Publication Decade"
    ]
]

y = df["Edition Category"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Feature Importance
importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print(feature_importance)

# Plot
plt.figure(figsize=(10,6))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"],
    color="green",
    edgecolor="black"
)

plt.title(
    "Feature Importance in Random Forest",
    fontsize=18,
    weight="bold"
)

plt.xlabel("Features", fontsize=13)
plt.ylabel("Importance Score", fontsize=13)

plt.xticks(rotation=30)

# Show value on bars
for i, value in enumerate(feature_importance["Importance"]):
    plt.text(
        i,
        value + 0.005,
        f"{value:.2f}",
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "feature_importance.png",
    dpi=300
)

plt.show()

print("\nChart saved as feature_importance.png")