# 📚 Book Analytics Using Data Science

> End-to-End Data Science Capstone Project using **Python**, **Machine Learning**, **Open Library API**, and **Power BI**.

---

## 📖 Project Overview

This project demonstrates the complete Data Science workflow by collecting book data from the Open Library API, cleaning and analyzing the dataset, building a Machine Learning model, and developing an interactive Power BI dashboard.

The objective is to gain meaningful insights into books, authors, publication trends, and edition counts while predicting the **Edition Category** using a Random Forest Classifier.

---

## 🚀 Project Features

- 🌐 Data Collection using Open Library API
- 🧹 Data Cleaning & Preprocessing
- 📊 Exploratory Data Analysis (EDA)
- ⚙️ Feature Engineering
- 🤖 Machine Learning Classification
- 📈 Model Evaluation
- 📉 Feature Importance Analysis
- 📊 Interactive Power BI Dashboard

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Libraries | Pandas, NumPy, Matplotlib, Scikit-learn, Requests |
| Data Source | Open Library API |
| Visualization | Matplotlib, Power BI |
| Machine Learning | Random Forest Classifier |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

## 📂 Project Workflow

```
Open Library API
        │
        ▼
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning
(Random Forest)
        │
        ▼
Model Evaluation
        │
        ▼
Power BI Dashboard
```

---

# 📁 Project Structure

```
Book-Analytics-Using-Data-Science
│
├── Dataset
│   ├── books_raw.csv
│   └── books_feature_engineered.csv
│
├── Source_Code
│   ├── openlibrary_scraper.py
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── feature_engineering.py
│   ├── ml_preprocessing.py
│   ├── model_evaluation.py
│   ├── feature_importance.py
│   └── book_classifier.py
│
├── Visualizations
│
├── Dashboard
│   └── capstone_project_dashboard.pbix
│
├── Presentation
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📊 Exploratory Data Analysis

The project includes visualizations such as:

- Subject Distribution
- Books Published Over the Years
- Edition Count Distribution
- Publication Year Distribution
- Top Authors
- Top Books by Editions
- Feature Importance
- Confusion Matrix

---

# 🤖 Machine Learning

### Algorithm

Random Forest Classifier

### Data Split

- Training Samples: **1501**
- Testing Samples: **376**

---

## 📈 Model Performance

| Metric | Value |
|---------|--------|
| Accuracy | **98.94%** |
| Precision | High |
| Recall | High |
| F1-Score | High |

---

## 📌 Important Features

The most influential features were:

- Edition Count
- Book Age
- Publication Year
- Publication Decade
- Subject
- Author

---

# 📊 Power BI Dashboard

The dashboard contains:

- KPI Cards
- Subject Distribution
- Publication Trends
- Top Authors
- Interactive Filters
- Dynamic Visualizations

---

# 📷 Project Screenshots

## Dashboard

> *(Add your Power BI Dashboard screenshot here.)*

---

## Subject Distribution

> *(Insert books_by_subject.png)*

---

## Publication Trends

> *(Insert books_by_year.png)*

---

## Top Authors

> *(Insert top_10_authors.png)*

---

## Feature Importance

> *(Insert feature_importance.png)*

---

# ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/book-analytics-data-science.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run scraper

```bash
python Source_Code/openlibrary_scraper.py
```

Run preprocessing

```bash
python Source_Code/data_cleaning.py
```

Run EDA

```bash
python Source_Code/eda_analysis.py
```

Run Machine Learning

```bash
python Source_Code/book_classifier.py
```

---

# 📚 Dataset

Source:

Open Library API

https://openlibrary.org/developers/api

---

# 📌 Future Improvements

- Deploy as a web application
- Add recommendation system
- Deep Learning model
- Real-time API integration
- Interactive Streamlit Dashboard

---

# 👨‍💻 Author

## Ritesh Redekar

B.Tech Computer Science & Engineering

### Connect with Me

- LinkedIn: www.linkedin.com/in/ritesh-redekar-94b5923b0
- GitHub: [https://github.com/YOUR-GITHUB](https://github.com/Ritesh-Redekar)

---

⭐ If you found this project useful, don't forget to star this repository.
