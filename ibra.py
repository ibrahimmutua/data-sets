# ===============================
# Basic Data Analysis and Visualization
# ===============================

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load Dataset
# Replace 'data.csv' with your dataset file
data = pd.read_csv('data.csv')

# 3. Explore Dataset
print("First 5 rows of the dataset:")
print(data.head())
print("\nDataset Info:")
print(data.info())
print("\nStatistical Summary:")
print(data.describe())

# 4. Check for Missing Values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# 5. Basic Analysis Examples

# Example 1: Count of unique values in a column
if 'Category' in data.columns:
    print("\nValue counts in 'Category' column:")
    print(data['Category'].value_counts())

# Example 2: Mean of a numerical column
if 'Sales' in data.columns:
    print("\nAverage Sales:", data['Sales'].mean())

# 6. Simple Visualizations

# Histogram of a numerical column
if 'Sales' in data.columns:
    plt.figure(figsize=(8,5))
    plt.hist(data['Sales'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Distribution of Sales")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.show()

# Bar chart of a categorical column
if 'Category' in data.columns:
    category_counts = data['Category'].value_counts()
    plt.figure(figsize=(8,5))
    category_counts.plot(kind='bar', color='lightgreen')
    plt.title("Count of Each Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()

# Scatter plot example (if numerical columns exist)
if 'Sales' in data.columns and 'Profit' in data.columns:
    plt.figure(figsize=(8,5))
    plt.scatter(data['Sales'], data['Profit'], color='coral')
    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.show()

# 7. Observations
print("\nObservations:")
print("- Check the distribution of numerical variables using histograms.")
print("- Look for relationships between columns using scatter plots.")
print("- Identify missing values for data cleaning before analysis.")
