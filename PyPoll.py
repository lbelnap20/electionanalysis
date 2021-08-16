#Resources/election_results.csv

#total number of votes cast
    #loop through and count number of ballot IDs
#Complete list of candidates who got votes
    #use a loop to store names in a dictionary; names are the key
#Total number of votes each candidate got
    #use same loop to store values in dictionary 
#percentage of votes for each candidate
    # use stored dictionary values to calculate 
#winner based on popular vote
    # use stored dictionary values to calculate 

import csv
import os
    #load file from path
fileToLoad= os.path.join('Resources', 'election_results.csv')
    #save file to a path
fileToSave = os.path.join('Analysis', 'election_analysis.txt')
    #open and read file
with open(fileToLoad) as election_data:
    fileReader = csv.reader(election_data)

    #readand print the header row
    headers = next(fileReader)
    print(headers)