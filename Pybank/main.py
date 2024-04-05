import csv
import os

# Define the path to the CSV file
csv_file_path = os.path.join('Resources', 'budget_data.csv')

# Read data from CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header
    data = [[row[0], int(row[1])] for row in csvreader]

# Calculate total number of months
total_months = len(data)

# Calculate net total amount of Profit/Losses
net_total = sum(row[1] for row in data)

# Calculate changes in Profit/Losses and average change
changes = [data[i][1] - data[i-1][1] for i in range(1, len(data))]
total_change = sum(changes)
average_change = total_change / (total_months - 1)

# Find greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Get corresponding dates for greatest increase and decrease
increase_date = data[changes.index(greatest_increase) + 1][0]
decrease_date = data[changes.index(greatest_decrease) + 1][0]

# Prepare the analysis output
analysis_output = (
    "Financial Analysis\n"
    "-----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n"
)

# Print analysis to the terminal
print(analysis_output)

# Export results to a text file in the 'analysis' folder
output_folder = 'analysis'
output_file_path = os.path.join(output_folder, 'financial_analysis.txt')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(output_file_path, 'w') as output_file:
    output_file.write(analysis_output)

print(f"Analysis exported to {output_file_path}")
