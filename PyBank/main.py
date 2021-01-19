#PyBank Homework solution


#import modules
import os
import csv

#Create a variable for csv file
budget = "Resources/budget_data.csv"

# Tell the program to open the file, skip the header row, and create a list for each column with each row of information

with open(budget) as file:
    reader = csv.reader(file)
    header = next(reader)
    months = []
    profit = []
    
# Create loop to read through CSV file and track "Date" and "Profit/Losses" column data

    for row in reader:
        months.append(row[0])
        profit.append(float(row[1]))

#Calculate total months covered in date column
total_months = (len(months))

#Calculate the net total profit in the dates covered
tot_profit = sum(profit)


#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period