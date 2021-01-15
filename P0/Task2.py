"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

total_time_dict = defaultdict(int)

for i in calls:
	
	# add outgoing number : duration
	total_time_dict[i[0]] += int(i[3])

	# add calling number : duration
	total_time_dict[i[1]] += int(i[3])


		
# maximum time value
max_time = max(total_time_dict.values())

# phno. spent longest time
for phno, time in total_time_dict.items():
	if time == max_time:

		# print the message
		print(str(phno)+" spent longest time, " +str(time) + " seconds, on the phone during September 2016.")
