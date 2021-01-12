import os
import csv

num_months = 0
total_sum = 0
max_gain = 0
max_loss = 0
#initializing these variables to null string values
gain_month = None
loss_month = None

budget_csv = os.path.join('', 'Resources', 'budget_data.csv')


def display_data(month_gain, month_loss, maximum_gain, maximum_loss, sum_total, num_of_months):

	mean_amount = (sum_total / num_of_months)
	#round to the nearest 1/1000th
	mean_amount = round(mean_amount, 3)
	
	#have some blank space
	print(f"")
	print(f"")
	print(f"Financial Analysis")
	print(f"------------------------------------")
	print(f"Total Months: {num_of_months}")
	print(f"Total: {sum_total}")
	print(f"Average Change: {mean_amount} ")
	print(f"Greatest Gain in Profits: {month_gain}  (${maximum_gain})")
	print(f"Greatest Loss in Profits: {month_loss}  (${maximum_loss})")

	
		
with open(budget_csv, 'r') as csvfile:
	bank_reader = csv.reader(csvfile, delimiter=',')

	header = next(bank_reader)
	for row in bank_reader:
		num_months += 1
		total_sum += int(row[1])
		if (max_loss > int(row[1])):
			max_loss = int(row[1])
			loss_month = str(row[0])

		elif (max_gain < int(row[1])):
			max_gain = int(row[1])
			gain_month = str(row[0])
		
		else:
			max_loss = max_loss
			max_gain = max_gain
	
	display_data(gain_month, loss_month, max_gain, max_loss, total_sum, num_months)