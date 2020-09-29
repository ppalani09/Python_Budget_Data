#Load csv file

import csv

budgetData_CSV = "C:/Users/palan/NW-Data-Science/Python_Budget_Data/budget_data.csv"
budgetData_txtOutput = "C:/Users/palan/NW-Data-Science/Python_Budget_Data/budget_data_output.txt"

with open(budgetData_CSV) as csv_file:

    # Parse comma delimited data
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #initiatizing variables
    countRows = 0
    max_profitLoss_change = 0
    min_profitLoss_change = 0

    next(csv_file)

    # create row arrays (2 values per array)
    for row in csv_reader:

        # count total month (i.e. total rows) in array
        countRows = countRows + 1

        date = str(row[0])

        if countRows == 1:

            # initialize net profit/loss & set previous profit loss value
            net_profitLoss = int(row[1])
            profitLoss_prior = int(row[1])

        elif countRows > 1:

            # update net profit/loss
            net_profitLoss = net_profitLoss + int(row[1])

            # check for max profit/loss
            profitLoss_change = int(row[1]) - profitLoss_prior

            # set current row's profit loss to be previous row input for next iteration
            profitLoss_prior = int(row[1])

            if profitLoss_change > max_profitLoss_change:
                max_profitLoss_change = profitLoss_change
                max_date = str(row[0])
            elif profitLoss_change < min_profitLoss_change:
                min_profitLoss_change = profitLoss_change
                min_date = str(row[0])

    average_profitLoss = round(net_profitLoss / countRows,2)

    print(" \nFinancial Analysis \n----------------------------")
    print(f'Total Months: {countRows}')
    print(f'Total: ${net_profitLoss}')
    print(f'Average Change: ${average_profitLoss}')
    print(f'Greatest Increase In Profit: {max_date} (${max_profitLoss_change})')
    print(f'Greatest Decrease In Profit: {min_date} (${min_profitLoss_change})')

txt = open(budgetData_txtOutput,"w+")

with txt:

    txt.write("Financial Analysis \n----------------------------\n")
    txt.write(f'Total Months: {countRows}\n')
    txt.write(f'Total: ${net_profitLoss}\n')
    txt.write(f'Average Change: ${average_profitLoss}\n')
    txt.write(f'Greatest Increase In Profit: {max_date} (${max_profitLoss_change})\n')
    txt.write(f'Greatest Decrease In Profit: {min_date} (${min_profitLoss_change})\n')

txt.close()