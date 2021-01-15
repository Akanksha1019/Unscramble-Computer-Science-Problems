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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

l=[]
l=texts[0]
print("First record of texts,"+l[0]+" texts "+l[1]+" at time "+l[2])

print()
l1=[]
l1=calls[-1]
print("Last record of calls, "+l1[0]+" calls "+l1[1]+" at time "+l1[2]+", lasting "+l1[3] +" seconds")

print(len(l))
print(len(l1))


