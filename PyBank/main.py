# Import Libraries
import os
import csv

# Reading CSV data
csv_path = os.path.join("Resources", "budget_data.csv")

# Defining empty list for csv data
date_month = []
prof_loss = []

# Loading data and closing data file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Moving cursor to the second line
    csv_header = next(csv_reader)

    # Converting csv data into lists
    for row in csv_reader:
        date_month.append(row[0])
        prof_loss.append(row[1])

# Dictionary from lists
dictionary = dict(zip(date_month, prof_loss))
# Converting dictionary values to integers
dictionary = dict((k, int(v)) for k, v in dictionary.items())
# Calculating Total Months
tot_months = int(len(dictionary.keys()))
# Calculating Total Profit
tot_profit = sum(dictionary.values())
# Converting list values to integers
prof_loss = [int(i) for i in prof_loss]
# Calculating Average Profit Change (minus 1 month)
change = [prof_loss[i+1] - prof_loss[i] for i in range(len(prof_loss)-1)]
avg_change = round((sum(change) / len(change)), 2)
# Dropping first month in the list (since difference calculated starting from the second month)
date_month.pop(0)
# New dictionary with profit changes per month
change_dict = dict(zip(date_month, change))
# Calculating Max Profit Increase along with corresponding month
max_incr = max(change_dict.values())
max_incr_month = str(
    [k for k, v in change_dict.items() if v == max_incr])[2:-2]
# Calculating Max Profit Decrease along with corresponding month
max_decr = min(change_dict.values())
max_decr_month = str(
    [k for k, v in change_dict.items() if v == max_decr])[2:-2]

# Printing to terminal
print("\n```text")
print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: $ {tot_profit}")
print(f'Average Change: ${avg_change}')
print(f"Greatest Increase in Profits: {max_incr_month} (${max_incr})")
print(f"Greatest Decrease in Profits: {max_decr_month} (${max_decr})")
print("```")

# Output to txt file
file_to_output = os.path.join("Analysis", "budget_analysis.txt")
l1 = "\n```text"
l2 = "Financial Analysis"
l3 = "---------------------------------------------------"
l4 = f"Total Months: {tot_months}"
l5 = f"Total: $ {tot_profit}"
l6 = f'Average Change: ${avg_change}'
l7 = f"Greatest Increase in Profits: {max_incr_month} (${max_incr})"
l8 = f"Greatest Decrease in Profits: {max_decr_month} (${max_decr})"
l9 = "```"

output = f'{l1} \n{l2} \n{l3} \n{l4} \n{l5} \n{l6} \n{l7} \n{l8} \n{l9}'
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
