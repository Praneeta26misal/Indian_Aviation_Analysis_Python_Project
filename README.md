
Indian Aviation Analysis 

A Python-based data analysis project exploring Indian domestic flight schedules from 2018–2025. The project uses Pandas for data cleaning and analysis and Matplotlib for visualizing patterns in airlines, airports, routes, and flight departure timings.

Project Overview

The goal of this project was to explore Indian domestic aviation data and understand patterns such as:

- Airline activity and network coverage
- Most active departure airports
- Popular flight routes
- Flight departure-time patterns
- Airport and route connectivity

Tools & Technologies

- Python
- Pandas
- Matplotlib
- CSV

Dataset

The project uses publicly available Indian aviation flight schedule data covering the period from 2018–2025.

The raw dataset contains information related to airlines, flight numbers, origins, destinations, validity dates, and scheduled departure times.

Data Preparation

Before analysis, the dataset was inspected and cleaned using Pandas.

The main preprocessing steps included:

- Inspecting the dataset structure and columns
- Checking for missing values
- Checking for duplicate records
- Removing duplicate rows
- Converting date fields into datetime format
- Removing records missing important flight information such as airline, flight number, origin, or destination
- Converting scheduled departure times into a usable format for analysis

Analysis

The project explored several aspects of the Indian domestic aviation network.

Airline Analysis

Analyzed the number of flights for different airlines to identify those with a larger presence in the dataset.

Airport Analysis

Analyzed departure airports to identify airports with higher flight activity and understand patterns in airport connectivity.

Route Analysis

Examined origin-destination combinations to identify frequently operated flight routes and understand route patterns across the domestic network.

Departure Time Analysis

Analyzed scheduled departure times to understand how flights are distributed throughout the day.

Visualizations

The project includes visualizations such as:

- Top airlines by number of flights
- Top departure airports
- Top flight routes
- Flights by departure hour
￼
Project Structure:

indian-aviation-analysis/
│
├── aviation_analysis.py
├── Air_full-Raw.csv
├── Air_cleaned.csv
├── airline_summary.csv
├── departure_summary.csv
├── top_routes.csv
│
├── flights_by_departure_hour.png
├── top_10_airlines_by_nums.png
├── top_airlines.png
├── top_departure_airports.png
│
└── .gitignore
