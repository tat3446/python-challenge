# Modules
import os
import csv

date = []

#Set path for file
bank_csv = os.path.join("Resources", "budget_data.csv")

#Set variables
#month_total = 0
#Prof_Loss_total = 0
#prof_loss_chg = 0

#prof_loss = []
#prof_loss_chg = []
#Prof_Loss_total = []

#Read the csv file
with open(bank_csv) as bank_list:

    #CSV reader to translate contents of file
    csvreader = csv.reader(bank_list)

    #Read in header of file
    csvheader = next(csvreader)
    
    #Read in data rows
    for row in csvreader:
        if row[2] not in date:
            date.append(row[2])

print(date)






