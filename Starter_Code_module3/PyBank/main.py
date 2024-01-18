import os
import csv

#Reads CSV file
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

#opens budget_csv as csvfile
with open(budget_csv) as csvfile:
    #reads the csv file
    csvreader = csv.reader(csvfile, delimiter=",") 
    #Define variables 
    months = 0
    profits = []
    month = []
    profit_change = []
    #skip header
    header = next(csvreader)
    #loops through rows
    for row in csvreader:
        #add up months
        months = months + 1
        #store profits in a list
        profits.append(float(row[1]))
        month.append(row[0])

    for i in range(len(profits)-1):
        profit_change.append(profits[i+1]-profits[i])


#add up profits 
net_profits = sum(profits)
#find max profit
max_profit = max(profit_change)
max_month = profit_change.index(max(profit_change)) +1
#find min profit 
min_profit = min(profit_change)
min_month = profit_change.index(min(profit_change)) +1

#find average profit change
average_profit_change = (sum(profit_change)/len(profit_change))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(months)}")
print(f"Total: ${net_profits}")
print(f"Average Change: ${average_profit_change}")
print(f"Greatest Increase in Porfits: {month[max_month]} ${max_profit}")
print(f"Greatest Decrease in Porfits: {month[min_month]} ${min_profit}")

output_path = os.path.join("..", "PyBank", "pybank_analysis.csv")

with open(output_path,"w") as file:
    csvwriter = csv.writer(file, delimiter=',')
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {str(months)}")
    file.write("\n")
    file.write(f"Total: ${net_profits}")
    file.write("\n")
    file.write(f"Average Change: ${average_profit_change}")
    file.write("\n")
    file.write(f"Greatest Increase in Porfits: {month[max_month]} ${max_profit}")
    file.write("\n")
    file.write(f"Greatest Decrease in Porfits: {month[min_month]} ${min_profit}")