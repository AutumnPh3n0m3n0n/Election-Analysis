import os
import csv

total_votes = 0
Khan = 0
Correy = 0
Lai = 0
OTooley = 0


election_csv = os.path.join('', 'Resources', 'election_data.csv')

#can is short for candidate
#pol is short for politician
def gather_results(pol1, pol2, pol3, pol4, can1, can2, can3, can4, can_total):
	candidate1 = (can1 / can_total) * 100
	candidate2 = (can2 / can_total) * 100
	candidate3 = (can3 / can_total) * 100
	candidate4 = (can4 / can_total) * 100
	#round to nearest 1/1000th
	candidate1 = round(candidate1, 3)
	candidate2 = round(candidate2, 3)
	candidate3 = round(candidate3, 3)
	candidate4 = round(candidate4, 3)
	
	#have some blank space
	print(f"")
	print(f"")
	
	print(f"------------------------------------")
	print(f"Election Polling Results")
	print(f"------------------------------------")
	print(f"Total Votes: {can_total}")
	print(f"------------------------------------")
	print(f"{pol1} : {candidate1} % ({can1})")
	print(f"{pol2} : {candidate2} % ({can2})")
	print(f"{pol3} : {candidate3} % ({can3})")
	print(f"{pol4} : {candidate4} % ({can4})")
	print(f"------------------------------------")
	
	#can1 is Khan
	#can2 is Correy
	#can3 is Lai
	#Can4 is OTooley
	if ((can1 > can2) or (can1 > can3) or (can1 > can4)):
		print(f"WINNER: {pol1}")
	elif ((can2 > can1) or (can2 > can3) or (can2 > can4)):
		print(f"WINNER: {pol2}")
	elif ((can3 > can1) and (can3 > can2) and (can3 > can4)):
		print(f"WINNER: {pol3}")
	else:
		print(f"WINNER: {pol4}")
		
	print(f"------------------------------------")


# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    election_reader = csv.reader(csvfile, delimiter=',')

	#skip a row for the header arguments
    header = next(election_reader)
    for row in election_reader:
	    total_votes += 1
	    if (row[2] == "Khan"):
		    Khan += 1
	    elif (row[2] == "Correy"):
		    Correy += 1
	    elif (row[2] == "Li"):
		    Lai += 1
	    else:
		    OTooley += 1
			
    gather_results("Khan", "Correy", "Li", "OTooley", Khan, Correy, Lai, OTooley, total_votes)
	