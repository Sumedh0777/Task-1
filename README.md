
# Task 1 – Data Cleaning and Preprocessing

## 📌 Objective
To clean and preprocess a raw dataset by removing duplicates, handling missing values, standardizing formats, and correcting data types.

## 📂 Dataset Used
**Mall Customer Segmentation Data** (simulated version for internship task)

## 🧼 Cleaning Steps Performed

1. **Removed duplicate rows**
2. **Dropped rows with missing values** in `CustomerID` and `Age`
3. **Standardized text values** in the `Gender` column (e.g., 'MALE' → 'male')
4. **Renamed column headers** to lowercase, snake_case format
5. **Converted date formats** in the `join_date` column to `YYYY-MM-DD`
6. **Checked and corrected data types** for `CustomerID`, `Age`, and `Join_Date`

---

## ❓ Interview Questions & Answers

### 1. What are missing values and how do you handle them?
Missing values are blanks or null entries in the dataset. They can be handled by removing rows (`dropna()`), filling them with statistical values (`fillna()`), or imputing based on business logic.

### 2. How do you treat duplicate records?
Duplicate records can be detected using `duplicated()` and removed using `drop_duplicates()`. In Excel, you can use "Remove Duplicates" under the Data tab.

### 3. Difference between `dropna()` and `fillna()` in Pandas?
- `dropna()` removes rows or columns with missing values.
- `fillna()` fills missing values with a specified value (e.g., mean, median).

### 4. What is outlier treatment and why is it important?
Outliers are unusual data points that can skew analysis. Treatment includes removing them or capping them using statistical methods like IQR or Z-score.

### 5. Explain the process of standardizing data.
Standardizing involves converting text (e.g., 'Male', 'MALE') to a consistent format and ensuring dates, numbers, and categories follow uniform standards.

### 6. How do you handle inconsistent data formats (e.g., date/time)?
Use tools like `pd.to_datetime()` in Pandas or format functions in Excel to convert inconsistent date strings into a standard format.

### 7. What are common data cleaning challenges?
- Missing values
- Duplicates
- Inconsistent formats
- Wrong data types
- Invalid or outlier values

### 8. How can you check data quality?
By checking for:
- Null values
- Duplicates
- Inconsistent entries
- Unexpected data types or ranges

---

## ✅ Result
The dataset is cleaned and ready for further analysis or modeling.

---

## 📁 Files Included

- `mall_customers_raw.csv`
- `cleaned_mall_customers.csv`
- `data_cleaning_script.py`
- `README.md`
