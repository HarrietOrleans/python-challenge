# Import library
import os
import csv

# file path
budget_csv = '../python-challenge/PyBank/Resources/budget_data.csv'

# variables
total_months = 0
net_total = 0
changes = []
months = []
previous_profit_loss = None
greatest_increase = {'date': None, 'amount': float('-inf')}
greatest_decrease = {'date': None, 'amount': float('inf')}

# Open and read file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip header
    next(csvreader)
    
    # Run through each row after the header
    for row in csvreader:
        month, profit_loss = row
        profit_loss = int(profit_loss)
        
        # Number of months
        total_months += 1
        
        # Net total amount of "Profit/Losses"
        net_total += profit_loss
        
        if previous_profit_loss is not None:
            # Change from the previous month
            change = profit_loss - previous_profit_loss
            changes.append(change)
            months.append(month)
            
            # Greatest increase in profits
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = month
            
            # Greatest decrease in profits
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = month
        
        previous_profit_loss = profit_loss

# Average change
average_change = sum(changes) / len(changes) if changes else 0

# Print results
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

print(results)

# Export results
output_file = '../python-challenge/PyBank/Analysis/financial_analysis.txt'
with open(output_file, 'w') as textfile:
    textfile.write(results)
