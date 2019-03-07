import os
import csv
import statistics

#declare file path for csv
csvpath = os.path.join('./budget_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #read and skip headers
    csv_header = next(csv_reader)
    # print(csv_header)

    # declare variables
    month = []
    amount = []
    amount_change = []

    # seperate data
    for row in csv_reader:
        month.append(row[0])
        amount.append(row[1])

# get number of entries
entries = len(month)
# convert string list to int
amount = list(map(int, amount))
profit = sum(amount)

# get change on a per month basis
for i in range(1,entries,1):
    change = amount[i] - amount[i-1]
    amount_change.append(change)

amount_avg = statistics.mean(amount_change)

# get max and min profits
max_profit = max(amount_change)
max_date = month[amount_change.index(max(amount_change))+1]
min_profit = min(amount_change)
min_date = month[amount_change.index(min(amount_change))+1]

# print results
print('Financial Results:')
print('Total Months: {}'.format(entries))
print('Total Proft: ${:,}'.format(profit))
print('Average Change: ${:,.2f}'.format(amount_avg))
print('Max Profit: ${:,} on {}'.format(max_profit, max_date))
print('Min Profit: ${:,} on {}'.format(min_profit, min_date))
