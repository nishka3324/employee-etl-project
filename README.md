# Healthcare Analytics ETL Project

## Project Overview

Built an end-to-end healthcare analytics pipeline using Python, Pandas, PostgreSQL, SQL, Tableau, and GitHub.

The project processes healthcare records, performs data cleaning and transformation, loads the data into PostgreSQL, and visualizes key healthcare metrics through an interactive Tableau dashboard.

## Dataset

* 55,500 healthcare records
* 15 original columns
* 54,966 records after cleaning
* 534 duplicate records removed

## Technologies Used

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* SQL
* Tableau Public
* Git & GitHub

## ETL Process

### Extract

* Read healthcare dataset from CSV

### Transform

* Removed duplicate records
* Standardized column names
* Converted date fields
* Created `length_of_stay` metric

### Load

* Loaded cleaned dataset into PostgreSQL

## Analysis Performed

* Patient count by medical condition
* Average billing amount by condition
* Gender distribution
* Admission type analysis
* Average length of stay

## Results

Created an interactive Tableau dashboard to analyze patient demographics, billing trends, hospital admissions, and healthcare outcomes.
