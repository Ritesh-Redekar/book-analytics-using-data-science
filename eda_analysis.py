import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_raw.csv")

print("="*60)
print("EXPLORATORY DATA ANALYSIS")
print("="*60)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe(include="all"))

# -----------------------------
# Chart 1 : Number of Books by Subject
# -----------------------------
subject_counts = df["Subject"].value_counts()

plt.figure(figsize=(10,6))

subject_counts.plot(
    kind="bar",
    color="steelblue",
    edgecolor="black"
)

plt.title("Number of Books by Subject", fontsize=15)
plt.xlabel("Subject")
plt.ylabel("Number of Books")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("books_by_subject.png", dpi=300)

plt.show()

print("\nChart saved as books_by_subject.png")

# ---------------------------------------------------------
# Chart 2 : Top 10 Authors by Number of Books
# ---------------------------------------------------------

# Count books written by each author
top_authors = df["Author"].value_counts().head(10)

# Create figure
plt.figure(figsize=(12, 6))

# Create bar chart
bars = plt.bar(
    top_authors.index,
    top_authors.values,
    color="orange",
    edgecolor="black",
    width=0.7
)

# Add title
plt.title(
    "Top 10 Authors by Number of Books",
    fontsize=17,
    fontweight="bold"
)

# Axis labels
plt.xlabel("Author", fontsize=12)
plt.ylabel("Number of Books", fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=45, ha="right")

# Add horizontal grid
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Add value labels above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

# Adjust layout
plt.tight_layout()

# Save chart
plt.savefig("top_10_authors.png", dpi=300)

# Display chart
plt.show()

print("\n✓ Chart saved as top_10_authors.png")

# ==========================================
# CHART 3 - BOOKS BY PUBLICATION YEAR
# ==========================================

import matplotlib.pyplot as plt

# Remove invalid years
year_df = df[
    (df["Publish Year"] > 1500) &
    (df["Publish Year"] <= 2025)
]

# Count books by year
year_counts = year_df["Publish Year"].value_counts().sort_index()

plt.figure(figsize=(14,6))

plt.plot(
    year_counts.index,
    year_counts.values,
    color="green",
    linewidth=2
)

plt.title(
    "Books Published Over the Years",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Publication Year", fontsize=14)
plt.ylabel("Number of Books", fontsize=14)

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "books_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved as books_by_year.png")

# =====================================================
# CHART 4 - TOP 10 SUBJECT DISTRIBUTION (PIE CHART)
# =====================================================

# Count books in each subject
subject_counts = df["Subject"].value_counts()

# Select Top 10 Subjects
top_subjects = subject_counts.head(10)

# Explode the largest slice
explode = [0.08] + [0]*(len(top_subjects)-1)

# Create figure
plt.figure(figsize=(11,9))

# Create pie chart
wedges, texts, autotexts = plt.pie(
    top_subjects.values,
    labels=top_subjects.index,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode,
    shadow=True,
    textprops={"fontsize":11}
)

# Make percentage text bold
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_weight("bold")
    autotext.set_color("black")

# Title
plt.title(
    "Top 10 Subjects Distribution",
    fontsize=20,
    fontweight="bold",
    pad=20
)

# Keep circle shape
plt.axis("equal")

# Legend
plt.legend(
    wedges,
    top_subjects.index,
    title="Subjects",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=10,
    title_fontsize=11
)

# Adjust layout
plt.tight_layout()

# Save image
plt.savefig(
    "subject_distribution_pie.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

# Show chart
plt.show()

print("\n✓ Chart saved as subject_distribution_pie.png")

# =====================================
# Chart 5: Edition Count Distribution
# =====================================

plt.figure(figsize=(12,6))

plt.hist(
    df["Edition Count"],
    bins=30,
    color="skyblue",
    edgecolor="black"
)

plt.title(
    "Distribution of Book Edition Counts",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.xlabel(
    "Edition Count",
    fontsize=14
)

plt.ylabel(
    "Number of Books",
    fontsize=14
)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "edition_count_distribution.png",
    dpi=300
)

plt.show()

print("\nChart saved as edition_count_distribution.png")

# =====================================
# Chart 6: Top 10 Books by Edition Count
# =====================================

top_books = (
    df.sort_values("Edition Count", ascending=False)
      .head(10)
)

plt.figure(figsize=(12,7))

bars = plt.barh(
    top_books["Title"],
    top_books["Edition Count"],
    color="mediumseagreen",
    edgecolor="black"
)

plt.title(
    "Top 10 Books by Edition Count",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.xlabel(
    "Edition Count",
    fontsize=14
)

plt.ylabel(
    "Book Title",
    fontsize=14
)

plt.grid(axis="x", linestyle="--", alpha=0.5)

# Highest at top
plt.gca().invert_yaxis()

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 20,
        bar.get_y() + bar.get_height()/2,
        f"{int(width)}",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

plt.tight_layout()

plt.savefig(
    "top_10_books_by_editions.png",
    dpi=300
)

plt.show()

print("\nChart saved as top_10_books_by_editions.png")

# =====================================
# Chart 7: Publication Year Box Plot
# =====================================

plt.figure(figsize=(10,6))

plt.boxplot(
    df["Publish Year"],
    vert=False,
    patch_artist=True,
    boxprops=dict(facecolor="skyblue", color="black"),
    medianprops=dict(color="red", linewidth=2),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
    flierprops=dict(
        marker="o",
        markerfacecolor="orange",
        markersize=5,
        markeredgecolor="black"
    )
)

plt.title(
    "Distribution of Publication Years",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.xlabel(
    "Publication Year",
    fontsize=14
)

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "publication_year_boxplot.png",
    dpi=300
)

plt.show()

print("\nChart saved as publication_year_boxplot.png")