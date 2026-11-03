# ApexPlanet Internship – Task 1: Data Immersion & Wrangling

## Project Overview

This project is part of the 60-Day Data Analytics Internship at ApexPlanet Software Pvt. Ltd.

The objective of this task is to understand, assess, clean, and transform a sales dataset into a structured and analysis-ready format using Python and Pandas.

## Objectives

- Understand the dataset structure and variables.
- Create a detailed data dictionary.
- Identify missing values and duplicate records.
- Perform data quality assessment.
- Detect invalid values and outliers.
- Clean and transform the dataset.
- Export the final cleaned dataset.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Google Colab
- Microsoft Excel
- GitHub

## Dataset Information

- Total Records: 1,000
- Total Columns: 12 (original dataset)
- Dataset Type: Sales Transactions
- File Format: Excel (.xlsx)

## Data Quality Assessment

The following issues were identified:

| Issue | Findings |
|---|---:|
| Missing Age values | 20 |
| Missing City values | 13 |
| Exact duplicate rows | 0 |
| Repeated Order ID records | 9 |
| Invalid dates | 0 |
| Sales calculation errors | 0 |
| Sales outliers | 19 |

## Data Cleaning & Transformation

The following operations were performed:

1. Handled missing Age values using median imputation.
2. Replaced missing City values with "Unknown".
3. Converted Order_Date into datetime format.
4. Removed unnecessary leading and trailing spaces from text columns.
5. Investigated repeated Order_ID records and preserved them.
6. Created unique Transaction_Row_ID values.
7. Added flags to identify repeated Order IDs and sales outliers.
8. Validated Total_Sales calculations.

## Final Results

- 1,000 records preserved.
- 0 missing values after cleaning.
- 0 exact duplicate rows.
- 1,000 unique transaction row identifiers.
- 19 sales outliers flagged for investigation.
- Final cleaned dataset exported as CSV.

## Project Deliverables

- Cleaned Sales Dataset
- Data Dictionary
- Data Quality Report
- Python Data Cleaning Script
- Google Colab Notebook

## Conclusion

This project provided practical experience in data familiarization, data quality assessment, data cleaning, and transformation using Python and Pandas.

The final dataset is structured and prepared for further exploratory data analysis.

---

**Internship:** ApexPlanet Data Analytics Internship  
**Task:** Task 1 – Data Immersion & Wrangling  
**Tools:** Python, Pandas, NumPy, Google Colab
