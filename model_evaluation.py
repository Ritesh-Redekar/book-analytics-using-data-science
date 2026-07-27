import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load dataset
df = pd.read_csv("books_feature_engineered.csv")

# Encode categorical columns
author_encoder = LabelEncoder()
subject_encoder = LabelEncoder()
target_encoder = LabelEncoder()

df["Author"] = author_encoder.fit_transform(df["Author"])
df["Subject"] = subject_encoder.fit_transform(df["Subject"])
df["Edition Category"] = target_encoder.fit_transform(df["Edition Category"])

# Features and target
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
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7,6))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=target_encoder.classes_
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix")

plt.savefig(
    "confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Chart saved as confusion_matrix.png")