# Import Libraries
import os
import csv

# Reading CSV data
csv_path = os.path.join("Resources", "election_data.csv")

# Defining empty list for csv data
voter_id = []
county = []
candidate = []

# Loading data and closing data file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Moving cursor to the second line
    csv_header = next(csv_reader)

    # Converting csv data into lists
    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

tot_votes = int(len(voter_id))
list_candidates = list(set(candidate))
correy = [e for e in candidate if e == 'Correy']
khan = [e for e in candidate if e == 'Khan']
li = [e for e in candidate if e == 'Li']
otooley = [e for e in candidate if e == "O'Tooley"]

correy_perc = (len(correy) / tot_votes * 100)
khan_perc = (len(khan) / tot_votes * 100)
li_perc = (len(li) / tot_votes * 100)
otooley_perc = (len(otooley) / tot_votes * 100)

# Printing to terminal
print("\n```text")
print("Election Results")
print("---------------------------------------------------")
print(f"Total Votes: {tot_votes}")
print(f"{khan[0]}: {round(khan_perc, 3)}% ({len(khan)})")
print(f"{correy[0]}: {round(correy_perc, 3)}% ({len(correy)})")
print(f"{li[0]}: {round(li_perc, 3)}% ({len(li)})")
print(f"{otooley[0]}: {round(otooley_perc, 3)}% ({len(otooley)})")
print("---------------------------------------------------")
print(f"Winner: {khan[0]}")
print("---------------------------------------------------")
print("```")
