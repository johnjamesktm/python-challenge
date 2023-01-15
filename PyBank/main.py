import csv
import os

# Some constants we may reuse through-out the program.
LINE_DIVIDER = "----------------------------"

# Path to the input file.
input_file = os.path.join("Resources", "budget_data.csv")

# Open the CSV file
with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Given CSV file has a header row.
    # Skipping the header row.
    #
    # Headers are:
    # ['Date', 'Profit/Losses']
    header = next(csv_reader)

    count_months = 0
    net_total = 0
    change_total = 0
    last_amount = 0

    greatest_increase = {
        "date": "",
        "amount": 0
    }
    greatest_decrease = {
        "date": "",
        "amount": 0
    }

    # Iterate through all the rows to perform analysis.
    for row in csv_reader:
        amount = int(row[1])
        net_total = net_total + amount

        # Start analysing change from the second data row.
        if count_months > 0:
            change = amount - last_amount
            change_total = change_total + change

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change

        last_amount = amount
        count_months = count_months + 1

    output = [
        "Financial Analysis",
        LINE_DIVIDER,
        f'Total Months: {count_months}',
        f'Total: ${net_total}',
        f'Average Change: ${(change_total / (count_months - 1)):.2F}',
        f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})',
        f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})'
    ]

    output_file = os.path.join("analysis", "output.txt")

    with open(output_file, 'w') as file:
        for output_line in output:
            print(output_line)
            file.write(output_line + os.linesep)
