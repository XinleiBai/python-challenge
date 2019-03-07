import os
import csv

#declare file path for csv
csvpath = os.path.join('./election_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #read and skip headers
    csv_header = next(csv_reader)

    # declare variables and lists
    votes = []
    candidate_dict = {}

    for row in csv_reader:
        votes.append(row[2])

# get total number of votes
total = len(votes)
print('Total Votes: {:,}'.format(total))
# get unique value for candidates
candidates = set(votes)

# set candidates to dictionary keys
candidate_dict = dict((candidate,0) for candidate in candidates)

# increment votes
for vote in votes:
    if vote in candidate_dict:
        candidate_dict[vote] += 1

    else:
        break
# get max value
winner_val = max(candidate_dict.values())

# cycle through dictionary per candidate
for candidate,votes in candidate_dict.items():
    win_percentage = votes / total*100
    print('{}: %{:.2f}, #Votes: {:,}'.format(candidate,win_percentage,votes))
    if int(winner_val) == int(votes):
        print('Winner: {}'.format(candidate))

