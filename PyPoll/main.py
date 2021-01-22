# Import modules
import os
import csv

# Create a variable for csv file
polling = "Resources/election_data.csv"

# Tell the program to open file, skip the header row, and create a list for listed variables
with open(polling) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    candidates = []
    
    for row in reader:
        candidates.append(row[2])  

# Calculate total votes
total_votes = (len(candidates))

# Create a list of candidate names
candidate_names = list(set(candidates))

# Calculate the total votes won by each candidate
total_li = candidates.count("Li")
total_khan = candidates.count("Khan")
total_otooley = candidates.count("O'Tooley")
total_correy = candidates.count("Correy")

# Calculate the percent of votes won by each candidate
percent_li = total_li / total_votes
percent_khan = total_khan / total_votes
percent_otooley = total_otooley / total_votes
percent_correy = total_correy / total_votes

# Use mode to return highest vote count for candidates

from statistics import mode

def winner(candidates):
    return(mode(candidates))

# Print election results
print('Election Results')
print('-'*30)
print(f'Total Votes: {total_votes}')
print('-'*30)
print(f'Khan: {percent_khan:.3%} ({total_khan})')
print(f'Correy: {percent_correy:.3%} ({total_correy})')
print(f'Li: {percent_li:.3%} ({total_li})')
print(f"O'Tooley: {percent_otooley:.3%} ({total_otooley})")
print('-'*30)
print(f'Winner: {winner(candidates)}')

#Write election results to text file named "election.result" and save
with open('election.result.txt', 'w+') as txt:
    txt.write('Election Results \n')
    txt.write(f'--------------------------- \n')
    txt.write(f'Total Votes: {total_votes}\n')
    txt.write(f'--------------------------- \n')
    txt.write(f'Khan: {percent_khan:.3%} ({total_khan})\n')
    txt.write(f'Correy: {percent_correy:.3%} ({total_correy})\n')
    txt.write(f'Li: {percent_li:.3%} ({total_li})\n')
    txt.write(f"O'Tooley: {percent_otooley:.3%} ({total_otooley})\n")
    txt.write(f'--------------------------- \n')
    txt.write(f'Winner: {winner(candidates)}\n')
    txt.close