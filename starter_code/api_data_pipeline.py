"""
api_etl_pipeline.py
===================
Project:    API ETL Pipeline
Difficulty: Intermediate
Skills:     Python, requests, pandas, JSON handling, os module
Time:       Medium (2–5 days)

What you will build:
    Fetch data from a public API and automatically transform it into
    a clean, structured CSV dataset. The pipeline will validate API
    responses, normalize nested JSON data, handle missing values,
    generate summary statistics, and export the processed dataset
    for analytics, dashboards, or machine learning workflows.

    The final cleaned dataset and summary report are exported as files
    that can be reused for further data analysis projects.

How to run:
    pip install pandas requests
    python api_etl_pipeline.py

When prompted, enter a public API URL that returns JSON data.
A sample API endpoint is included at the bottom of this file
to help you test the project quickly without searching for APIs.

Learning goals:
    - Working with REST APIs using requests
    - Understanding JSON response structures
    - Extracting and normalizing nested API data
    - Converting JSON data into pandas DataFrames
    - Cleaning and transforming datasets
    - Exporting structured datasets to CSV files
    - Generating reusable summary reports

Roadmap:
    Step 1:  Run the script using the sample API endpoint
    Step 2:  Complete fetch_api_data() to retrieve JSON data safely
    Step 3:  Complete validate_response() to verify API responses
    Step 4:  Complete normalize_json() to flatten nested JSON data
    Step 5:  Complete create_dataframe() to build a pandas DataFrame
    Step 6:  Complete clean_data() to handle missing values and duplicates
    Step 7:  Complete export_csv() to save the processed dataset
    Step 8:  Complete generate_summary_report() to export statistics
    Step 9:  Test the pipeline with at least two different public APIs
"""