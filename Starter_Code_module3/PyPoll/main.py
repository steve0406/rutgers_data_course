import os
import csv

#Reads CSV file
election_csv = os.path.join(".", "Resources", "election_data.csv")

#opens budget_csv as csvfile
with open(election_csv) as csvfile:
    #reads the csv file
    csvreader = csv.reader(csvfile, delimiter=",") 
    #define variables to store
    vote = 0   
    votes = []
    vote_charles= []
    vote_c = 0
    vote_diana = []
    vote_d = 0
    vote_raymon = []
    vote_r = 0
    header = next(csvreader)
    #loops through the csv
    for row in csvreader:
        #countes votes
        vote = vote + 1
        #checks who the vote is vote and counts it
        if row[2] == 'Charles Casper Stockham':
              vote_charles.append(row[2])
              vote_c = vote_c + 1
        elif row[2] == 'Diana DeGette':
             vote_diana.append(row[2])
             vote_d = vote_d + 1
        elif row[2] == 'Raymon Anthony Doane':
            vote_raymon.append(row[2])
            vote_r = vote_r + 1

#calculates the percentages 
percent_charles = (vote_c/vote) * 100
percent_diana = (vote_d/vote) * 100
percent_raymon = (vote_r/vote) * 100
 

print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote}")
print("-------------------------")
print(f"Charles Casper Stockham: {percent_charles}% ({vote_c})")
print(f"Diana DeGette: {percent_diana}% ({vote_d})")
print(f"Raymon Anthony Doane: {percent_raymon}% ({vote_r})")
print("-------------------------")

#Checks to see who has the highest votes 
if vote_c > vote_d and vote_c>vote_r:
     print("Winner: Charles Casper Stockham")
     winner = "Winner: Charles Casper Stockham"
elif vote_d > vote_c and vote_d>vote_r:
     print("Winner: Diana DeGette")
     winner = "Winner: Diana DeGette"
else:  
     print("Winner: Raymon Anthony Doane")
     winner = "Winner: Charles Casper Stockham"
print("-------------------------")

output_path = os.path.join("..", "PyPoll", "pypoll_analysis.csv")

with open(output_path,"w") as file:
    csvwriter = csv.writer(file, delimiter=',')
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {vote}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {percent_charles}% ({vote_c})")
    file.write("\n")
    file.write(f"Diana DeGette: {percent_diana}% ({vote_d})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {percent_raymon}% ({vote_r})")
    file.write("\n")
    file.write(f"{winner}")
    file.write("\n")
    file.write("-------------------------")