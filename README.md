# Import CSV File into MySQL

This project provides scripts to generate sample data, configure MySQL connection, and import data from a CSV file into a MySQL database.

## Generate Sample Data

Run the `generate_csv.py` script to generate sample data in a CSV file.

```
python generate_csv.py
```
## Set up config.py
```
host = "localhost"
user = "root"
password = "your_password"
```
## After that, run the `csv_to_sql.py` to import data from a CSV file into a MYSQL database
```
python csv_to_sql.py
```

### Detailed Instructions for Each File:

- **generate_csv.py**:
  - Generates a CSV file containing sample data.

- **config.py**:
  - Contains the configuration settings for the MySQL connection, such as `host`, `user`, and `password`.

- **csv_to_sql.py**:
  - Imports data from the CSV file into the MySQL database, including checking and creating the database, creating the table, and inserting the data.

Ensure you have all necessary libraries installed and the MySQL server running before following the steps.
