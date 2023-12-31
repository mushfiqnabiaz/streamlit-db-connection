# Streamlit App with MySQL Integration

![Streamlit](https://img.shields.io/badge/Streamlit-0.89.0-brightgreen)
![MySQL](https://img.shields.io/badge/MySQL-5.7-blue)

A simple Streamlit web application that connects to a MySQL database and displays data in a DataTable.

## Introduction

This Streamlit web application demonstrates how to connect to a MySQL database and retrieve data to display in an interactive DataTable. It is a basic example that can serve as a starting point for more complex applications.

## Features

- Connects to a MySQL database.
- Retrieves data from a specific table.
- Displays the data in an interactive DataTable using Streamlit.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mushfiqnabiaz/streamlit-db-connection.git
cd streamlit-db-connection

2. Install the required packages

pip install streamlit mysql-connector-python pandas

3. Update the MySQL database credentials:
    Open the app.py file and replace the following placeholders with your actual database credentials:

host="your_host",
user="your_user",
password="your_password",
database="your_database"

4. Run the streamlit app

streamlit run app.py
