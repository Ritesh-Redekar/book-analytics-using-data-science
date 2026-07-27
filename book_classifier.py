import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv("books_feature_engineered.csv")

print("=" * 60)
print("DATASET LOADED")
print("=" * 60)

print(df.head())

# ---------------------------------------
# Encode Categorical Columns
# ---------------------------------------

label_author = LabelEncoder()
label_subject = LabelEncoder()
label_target = LabelEncoder()

df["Author"] = label_author.fit_transform(df["Author"])

df["Subject"] = label_subject.fit_transform(df["Subject"])

df["Edition Category"] = label_target.fit_transform(
    df["Edition Category"]
)

# ---------------------------------------
# Select Features
# ---------------------------------------

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

print("\nFeature Shape :", X.shape)
print("Target Shape :", y.shape)

# ---------------------------------------
# Train Test Split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ---------------------------------------
# Train Random Forest
# ---------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------------------------------
# Prediction
# ---------------------------------------

y_pred = model.predict(X_test)

# ---------------------------------------
# Accuracy
# ---------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL ACCURACY")
print("=" * 60)

print(f"Accuracy : {accuracy*100:.2f}%")

# ---------------------------------------
# Classification Report
# ---------------------------------------

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_target.classes_
    )
)

# ---------------------------------------
# Confusion Matrix
# ---------------------------------------

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, y_pred))