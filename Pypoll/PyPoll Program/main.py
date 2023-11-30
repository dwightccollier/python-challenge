import os
import csv

#makes use of the input path and creates an output path
csvpath = os.path.join("..", "Resources", "election_data.csv")

totalVotes = 0
Candidates = []
CandidateVotes = {}
WinningVote = 0
Winner = ""

#Opens file and iterates to where data is in the rows
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Gets total votes
        totalVotes += 1
        #Keeps track of the current Candidate
        Candidate = row[2]

        #Adds the Candidate to our database if we don't already have them
        if Candidate not in Candidates:
            Candidates.append(Candidate)
            CandidateVotes[Candidate] = 1
        #Gives our Candidate an additional vote
        CandidateVotes[Candidate] = CandidateVotes[Candidate] + 1




print("Election Results\n")
print("--------------------\n")
    #Printing out our Total Votes
print("Total Votes: %d\n" % totalVotes)
print("--------------------\n")

    #Gets the number of Votes for each Candidate
for Candidate in CandidateVotes:
        votes = CandidateVotes[Candidate]
        VoteP = float(votes)/float(totalVotes)*100
        #Keeps track of our winner
        if(votes > WinningVote):
            WinningVote = votes
            Winner = Candidate
        #Prints out each Candidate
        print("%s: " % Candidate)
        print("%d%% " % VoteP)
        print("(%d)\n" % votes)
print("--------------------\n")
print("Winner: %s\n" % Winner)
print("--------------------\n")