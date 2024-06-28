# import library
import os
import csv

#set file path
budget_csv = os.path.join("Resources", "budget_data.csv")

#set variables
total_months = 0
net_total = 0
changes = []
greatest_increase = {'date': None, 'amount': float('-inf')}
greatest_decrease = {'date': None, 'amount': float('inf')}

#open and read file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    #skip header
    next(csvreader)
    #exclude first month
    budget_csv = [next(csvreader)]
#print number of months
    for row in csvreader:
        total_months += 1
        print(total_months)
    

        