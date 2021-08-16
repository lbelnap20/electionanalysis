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

totalVotes = 0
candidate_options = []
candidate_votes = {}
winner =" "
winningCount = 0
winningPercent = 0

    #open and read file
with open(fileToLoad) as election_data:
    fileReader = csv.reader(election_data)

    #read  the header row
    headers = next(fileReader)
    #print each row
    for row in fileReader:
        totalVotes +=1 

        #get candidate names and add to list
        candidateName = row[2]
        if candidateName not in candidate_options:
            candidate_options.append(candidateName)
            #track votes
            candidate_votes[candidateName] = 0
        candidate_votes[candidateName] +=1

    #save results
with open(fileToSave, 'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        f"--------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    for candidateName in candidate_votes:
        votes = candidate_votes[candidateName]
        votePercent = float(votes) / float(totalVotes) * 100
        candidate_results = (f"{candidateName} received {votePercent:.2f}% of the vote.\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winningCount) and (votePercent > winningPercent):
            winningCount = votes
            winningPercent = votePercent
            winner = candidateName
        #winner of the vote
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winningCount:,}\n"
        f"Winning Percentage: {winningPercent:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)