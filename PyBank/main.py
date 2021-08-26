# Import Libraries
import os
import csv

# Reading CSV data
csv_path = os.path.join("Resources", "budget_data.csv")

# Defining empty list for csv data
date_mon = []
prof_loss = []


# Loading data and closing data file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Moving cursor to the second line
    csv_header = next(csv_reader)

    # Converting csv data into lists
    for row in csv_reader:
        date_mon.append(row[0])
        prof_loss.append(row[1])

dictionary = dict(zip(date_mon, prof_loss))
dictionary = dict((k, int(v)) for k, v in dictionary.items())
tot_months = int(len(dictionary.keys()))
tot_profit = sum(dictionary.values())
print(tot_profit)
