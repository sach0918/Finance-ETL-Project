# Finance ETL Pipeline with AWS S3, MySQL, and Streamlit Dashboard

## Project Overview

This project is a complete end-to-end Financial ETL (Extract, Transform, Load) and Analytics Pipeline built using Python, pandas, MySQL, AWS S3, and Streamlit.

The main objective of this project is to simulate a real-world data engineering workflow where stock market data is continuously fetched from an external financial API, transformed into a structured format, stored in cloud storage and databases, and finally visualized using an interactive analytics dashboard.

The project demonstrates how modern data pipelines work in production systems by integrating multiple technologies together into a single automated workflow.

---

# What This Project Does

This project performs the following tasks:

1. Extracts stock market data from the Alpha Vantage REST API
2. Converts the raw JSON response into pandas DataFrames
3. Cleans and transforms the data
4. Stores raw datasets as CSV files
5. Uploads datasets to AWS S3 cloud storage
6. Loads cleaned data into a MySQL database
7. Performs SQL-based analytical queries
8. Displays interactive visualizations using Streamlit

The dashboard allows users to:

* Compare multiple stocks
* Visualize stock price trends
* Analyze trading volume
* View top-performing stocks
* Interact with real-time filtered data

---

# Workflow Architecture

The complete workflow of the project is shown below:

API Extraction
↓
Data Transformation using pandas
↓
Data Cleaning and Validation
↓
CSV File Generation
↓
AWS S3 Cloud Upload
↓
MySQL Database Storage
↓
SQL Analytics Queries
↓
Streamlit Interactive Dashboard

---

# Technologies Used

## 1. Python

Python is used as the core programming language for building the ETL pipeline, integrating APIs, processing data, handling cloud uploads, and creating the dashboard.

---

## 2. Alpha Vantage API

The Alpha Vantage API is used to fetch daily stock market data such as:

* Opening price
* Closing price
* High price
* Low price
* Trading volume

The API returns data in JSON format which is later transformed into structured datasets.

---

## 3. pandas

The pandas library is used for:

* Data transformation
* Data cleaning
* DataFrame operations
* Handling missing values
* Datatype conversion
* Duplicate removal
* Time-series processing

pandas acts as the transformation layer of the ETL pipeline.

---

## 4. MySQL

MySQL is used as the structured relational database system for storing cleaned stock market data.

The database layer allows:

* Fast querying
* SQL analytics
* Aggregations
* Filtering
* Dashboard integration

The project also includes duplicate protection using SQL constraints.

---

## 5. AWS S3

Amazon S3 is used as cloud object storage for storing raw CSV files generated during the ETL process.

This simulates real-world cloud-based data lake storage architecture used in modern data engineering systems.

The pipeline uploads generated datasets to S3 automatically during execution.

---

## 6. Streamlit

Streamlit is used to build an interactive analytics dashboard.

The dashboard provides:

* Multi-stock comparison charts
* Trading volume visualization
* KPI metrics
* Top performer analysis
* Interactive filters

This creates a complete visualization layer on top of the ETL pipeline.

---

## 7. Logging

Python logging is used to monitor the complete pipeline execution.

The logs track:

* API request status
* Database connection status
* Inserted rows
* Duplicate rows
* Failed records
* AWS S3 upload status

Logging is an important production-level feature in real-world ETL systems.

---

# ETL Pipeline Explanation

## Extract Phase

During the extraction phase, stock market data is fetched from the Alpha Vantage REST API using HTTP requests.

The API response contains JSON data for multiple stock symbols.

Example symbols used:

* IBM
* NVDA
* MSFT
* TSLA

---

## Transform Phase

The extracted JSON data is converted into pandas DataFrames.

During transformation:

* Columns are renamed
* Data types are corrected
* Multiple stock datasets are merged
* Dates are standardized
* Numeric values are converted properly

This step converts raw API data into structured analytical data.

---

## Load Phase

After cleaning and validation:

* Data is stored as CSV files
* CSV files are uploaded to AWS S3
* Cleaned records are inserted into MySQL

The MySQL database acts as the analytics storage layer while S3 acts as cloud backup storage.

---

# Dashboard Features

The Streamlit dashboard includes:

* Interactive stock selection
* Multi-stock comparison charts
* Volume analysis charts
* Highest and lowest stock metrics
* SQL-powered analytics
* Dynamic filtering options

The dashboard directly connects with MySQL to fetch and visualize data in real time.

---

# Key Features of the Project

* End-to-End ETL Pipeline
* REST API Integration
* Data Cleaning and Transformation
* Cloud Storage using AWS S3
* MySQL Database Integration
* Logging and Error Handling
* Duplicate Protection
* Interactive Streamlit Dashboard
* SQL Analytics Queries
* Multi-Stock Comparison

---

# Future Improvements

Possible future improvements include:

* Real-time stock streaming
* Automated scheduling using Airflow
* Docker containerization
* CI/CD deployment
* Advanced financial indicators
* Candlestick visualizations
* Deployment on cloud platforms

---

# Conclusion

This project demonstrates a complete modern data engineering workflow by integrating APIs, data transformation, cloud storage, databases, analytics, and visualization into a single end-to-end pipeline.

The project simulates real-world ETL architecture and provides hands-on experience with practical data engineering concepts including cloud integration, structured storage, analytics processing, and dashboard development.
