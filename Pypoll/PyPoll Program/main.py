import os
import csv

#makes use of the input path and creates an output path
csvpath = os.path.join("D:/boot camp/Challenge/3rd challenge/starter code for challenge/PyPoll/PyPoll/Resources/election_data.csv")
outputFile = "D:/boot camp/Challenge/3rd challenge/starter code for challenge/PyPoll/PyPoll/analysis/output.txt"

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

#Originally I tried to get everything settled outside of this with function but found
#that doing it inside the function was much easier
with open(outputFile, 'w') as txtFile:

    txtFile.write("Election Results\n")
    txtFile.write("--------------------\n")
    #Printing out our Total Votes
    txtFile.write("Total Votes: %d\n" % totalVotes)
    txtFile.write("--------------------\n")

    #Gets the number of Votes for each Candidate
    for Candidate in CandidateVotes:
        votes = CandidateVotes[Candidate]
        VoteP = float(votes)/float(totalVotes)*100
        #Keeps track of our winner
        if(votes > WinningVote):
            WinningVote = votes
            Winner = Candidate
        #Prints out each Candidate
        txtFile.write("%s: " % Candidate)
        txtFile.write("%d%% " % VoteP)
        txtFile.write("(%d)\n" % votes)
    txtFile.write("--------------------\n")
    txtFile.write("Winner: %s\n" % Winner)
    txtFile.write("--------------------\n")