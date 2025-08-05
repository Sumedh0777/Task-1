
import pandas as pd
import numpy as np

# Load dataset
data = {
    'CustomerID': [1, 2, 3, 4, 4, 5, np.nan],
    'Gender': ['Male', 'Female', 'Female', 'MALE', 'MALE', 'female', 'Female'],
    'Age': [19, 21, 20, 23, 23, 31, None],
    'Annual Income (k$)': [15, 16, 17, 18, 18, 19, 20],
    'Spending Score (1-100)': [39, 81, 6, 77, 77, 40, 76],
    'Join_Date': ['2020-01-15', '15-02-2020', '03/03/2020', '2020/04/05', '2020/04/05', '', '2020-06-01']
}

df = pd.DataFrame(data)

# Drop duplicate rows
df = df.drop_duplicates()

# Drop rows with missing CustomerID or Age
df = df.dropna(subset=['CustomerID', 'Age'])

# Standardize Gender values
df['Gender'] = df['Gender'].str.lower().str.strip()

# Rename columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_')

# Convert Join_Date to datetime format
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce', dayfirst=True)

# Fix data types
df['customerid'] = df['customerid'].astype(int)
df['age'] = df['age'].astype(int)

# Save cleaned data
df.to_csv('cleaned_mall_customers.csv', index=False)
