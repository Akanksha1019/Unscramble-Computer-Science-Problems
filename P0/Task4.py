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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = set() 
recieving_calls = set()  
text_send = set() 
text_received = set()

for c in calls:
    outgoing_calls.add(c[0])
    recieving_calls.add(c[1])


for t in texts:
    text_send.add(t[0])
    text_received.add(t[1])
        

l = []
l= outgoing_calls - (recieving_calls or text_send or text_received)

telemarketers = sorted(l)
print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
	print(telemarketer)
