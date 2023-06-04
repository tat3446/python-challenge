# Modules
import os
import csv


#Set path for file
poll_csv = os.path.join("Resources","election_data.csv")

#Set variables
vote_total = 0
candidate = ""
candidates = []
count_candidates = {}
count = 0
percentage = float
winner = ""

# Read the csv file
with open(poll_csv) as poll_list:

    csvreader = csv.reader(poll_list)

    csvheader = next(csvreader)

    #Loop through list
    for row in csvreader:

        #Save ballot, county, and candidate
        ballot = row[0]
        county = str(row[1])
        candidate = str(row[2])

        vote_total += 1

        if candidate not in candidates:
            candidates.append(candidate)
            count_candidates[candidate] = 1

        else:
            count_candidates[candidate] +=1

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {vote_total}")
    print("----------------------------")

    #correct to print name and votes so far 
    for candidate,candidates in count_candidates.items():
        count = count_candidates[candidate]
        percentage = (count/vote_total) * 100
        print(f"{candidate}:  {percentage:.3f}%  ({count_candidates[candidate]}) ")

    print("----------------------------")
    winner = max(count_candidates, key=count_candidates.get)
    print(f"Winner: {winner}")
    print("----------------------------")
   
   #Export a text file with analysis results

    output_path = os.path.join("analysis","PyPoll.txt")
    with open(output_path, "w", encoding="utf-8") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f"Total Votes: {vote_total}\n")
        txtfile.write("----------------------------\n")
        for candidate,candidates in count_candidates.items():
            count = count_candidates[candidate]
            percentage = (count/vote_total) * 100     
            txtfile.write(f"{candidate}:  {percentage:.3f}%  ({count_candidates[candidate]})\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("----------------------------\n")
 