"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

a_c = set() #set of area Code

for c in calls:
	if c[0][:5] == "(080)": # area code of Bangalore

		if c[1][1] == "0": # add fixed line area codes between parentheses
			for i, v in enumerate(c[1]):
				if v == ")":
					a_c.add(c[1][:i+1])
		
		elif " " in c[1]: 
			a_c.add(c[1][:4]) # add mobile codes in list

		elif call[1][:3] == "140": # add Telemarketers code
			a_c.add("140")

codeList = sorted(list(a_c)) 
print("The numbers called by people in Bangalore have codes:")
for j in codeList:
	print(j)


## Part B

calls_bang_to_bang = 0 # no. of calls from Bangalore to Bangalore,
calls_bang_to_any = 0 # no. of calls from Bangalore to anywhere

for c in calls:

	if c[0][:5] == "(080)": # calls from Bangalore

		if c[1][:5] == "(080)": # calls to Bangalore
			calls_bang_to_bang += 1 
			calls_bang_to_any += 1

		else:
			calls_bang_to_any += 1 


percentage =(calls_bang_to_bang / calls_bang_to_any) * 100

print( "%.2f" % percentage+" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
