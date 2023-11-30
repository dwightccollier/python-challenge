import os
import csv
BankCsv = os.path.join("..","PyBank","Resources","budget_data.csv")




Months = 0
TotalRev = 0
MonthRev = []
ChangeRev = 0
PrevRev = 0
GreatestIncrease = ["",0]
GreatestDecrease = ["",0]
ChangeRevDic = []
Average = 0

with open(BankCsv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Total number of months
        Months += 1
        #Total amount of Revenue
        TotalRev = TotalRev + int(row[1])

        #calculating the total change
        ChangeRev = float(row[1])-PrevRev
        PrevRev = float(row[1])
        ChangeRevDic = ChangeRevDic + [ChangeRev]
        MonthRev.append(row[0])

        if GreatestDecrease[1] == 0:
            GreatestDecrease[1] = ChangeRev
            GreatestDecrease[0] = row[0]
        if ChangeRev > GreatestIncrease[1]:
            GreatestIncrease[1] = ChangeRev
            GreatestIncrease[0] = row[0]
        if ChangeRev < GreatestDecrease[1]:
            GreatestDecrease[1] = ChangeRev
            GreatestDecrease[0] = row[0]
    Average = sum(ChangeRevDic)/len(ChangeRevDic)

print("Financial Analysis")
print("---------------------")
print("Total Months: ",Months)
print("Total Revenue: ", TotalRev)
print("Average Revenue Change: $",Average,sep="")
print("Greatest Increase in Revenue: ",GreatestIncrease[0]," $",GreatestIncrease[1],sep="")
print("Greatest Decrease in Revenue: ",GreatestDecrease[0]," $",GreatestDecrease[1],sep="")

    