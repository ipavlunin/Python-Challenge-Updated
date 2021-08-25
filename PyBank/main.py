# Import Libraries
import os
import csv

# Reading CSV data
csv_path = os.path.join("Resources", "budget_data.csv")

total_months = []
total_amount = []


# Loading data and closing data file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Moving cursor to the second line
    csv_header = next(csv_reader)

    for row in csv_reader:
        print(row)
