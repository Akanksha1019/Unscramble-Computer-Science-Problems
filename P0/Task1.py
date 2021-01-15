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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

l=[]
for i in texts:
    l.append(i[0])
    l.append(i[1])

for i in calls:  
    l.append(i[0])
    l.append(i[1])
    
l= set(l)
print("There are " + str(len(l))+ " different telephone numbers in the records.") 
