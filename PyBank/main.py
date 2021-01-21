# PyBank Homework solution


# import modules
import os
import csv

# Create a variable for csv file
budget = "Resources/budget_data.csv"

# Tell the program to open the file, skip the header row, and create a list for each column with each row of information

with open(budget) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    months = []
    profit = []
    change = []
    
# Create loop to read through CSV file and track "Date" and "Profit/Losses" column data

    for row in reader:
        months.append(row[0])
        profit.append(float(row[1]))

# Calculate total months covered in date column
total_months = (len(months))

#C alculate the net total profit in the dates covered
tot_profit = sum(profit)

# Calclulate the change in Profit/Losses over the entire period by creating variables to solve for each
last_profit = profit[-1]
first_profit = profit[0]
avg_profit = (last_profit - first_profit) / (total_months - 1)


# Add greatest increase and decrease here


# Print the results in Terminal
print("Financial Analysis")
print('-'*30)
print(f'Total Months: {total_months}')
print(f'Total: {tot_profit}')
print(f'Average Change: {avg_profit}')
print(f'Greatest Increase in Profits: ')
print(f'Greatest Decrease in Profits: ')

# Write to new text file named "financial_analysis" and save