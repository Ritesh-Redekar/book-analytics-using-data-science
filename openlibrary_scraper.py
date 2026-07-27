import requests
import pandas as pd

# List of subjects to collect books from
subjects = [
    "fantasy",
    "science_fiction",
    "romance",
    "history",
    "mystery",
    "adventure",
    "horror",
    "children",
    "biography",
    "love",
    "thriller",
    "poetry",
    "drama",
    "comics",
    "fiction",
    "art",
    "music",
    "travel",
    "science",
    "technology",
    "education",
    "business",
    "philosophy",
    "psychology",
    "religion"
]

# Empty list to store all books
books = []

# Loop through each subject
for subject in subjects:

    print(f"Collecting books from: {subject}")

    # API URL for current subject
    url = f"https://openlibrary.org/subjects/{subject}.json?limit=100"

    # Send request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data for {subject}")
        continue

    # Convert JSON to Python dictionary
    data = response.json()

    # Get all books from this subject
    works = data.get("works", [])

    # Loop through each book
    for book in works:

        title = book.get("title", "N/A")

        # Author
        author = "Unknown"
        if "authors" in book and len(book["authors"]) > 0:
            author = book["authors"][0].get("name", "Unknown")

        # Publish Year
        publish_year = book.get("first_publish_year", "N/A")

        # Edition Count
        edition_count = book.get("edition_count", 0)

        # Subject
        subject_name = subject.replace("_", " ").title()

        # Open Library ID
        work_id = book.get("key", "N/A")

        # Add book to list
        books.append({
            "Title": title,
            "Author": author,
            "Publish Year": publish_year,
            "Edition Count": edition_count,
            "Subject": subject_name,
            "Work ID": work_id
        })

# Convert list to DataFrame
df = pd.DataFrame(books)

# Remove duplicate books
df.drop_duplicates(subset=["Work ID"], inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Save dataset
df.to_csv("books_raw.csv", index=False)

# Display summary
print("\n======================================")
print("Dataset created successfully!")
print("Total Books Collected:", len(df))
print("======================================\n")

# Display first 10 rows
print(df.head(10))