# Modules
import os
import csv
import sys

prof_loss_chg = []
prof_loss_list = []

#Set path for file
bank_csv = os.path.join("Resources","budget_data.csv")

#Set variables
prof_loss_total = 0
month_total = 0
prior_profloss = 0.00
prof_loss_avg = 0.00
max_change = 0
max_month = ""
min_change = 0
min_month = ""

# #Read the csv file
with open(bank_csv) as bank_list:
    
    #CSV reader to translate contents of file
    csvreader = csv.reader(bank_list)
     
    #Read in header of file
    csvheader = next(csvreader)

    #Loop through list
    for row in csvreader:

        #save date and amount
        date = row[0]
        amount = int(row[1])

        month_total += 1
        prof_loss_total += amount
        
        #Calculate change in Profit/Losses
        if month_total > 1:

            prof_loss_chg = amount - prior_profloss
            prof_loss_list.append(prof_loss_chg)

            if prof_loss_chg > max_change:
                max_change = prof_loss_chg
                max_month = date
                
            if prof_loss_chg < min_change:
                min_change = prof_loss_chg
                min_month = date

        prior_profloss = amount

    prof_loss_avg = sum(prof_loss_list) / (month_total-1)

#Print statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${prof_loss_total}")
print(f"Average Change: ${prof_loss_avg:.2f}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

#Export a text file with analysis results

output_path = os.path.join("analysis","PyBank.txt")
with open(output_path, "w", encoding="utf-8") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {month_total}\n")
    txtfile.write(f"Total: ${prof_loss_total}\n")
    txtfile.write(f"Average Change: ${prof_loss_avg:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_month} (${min_change})\n")
