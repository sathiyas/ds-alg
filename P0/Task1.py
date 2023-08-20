"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
unique_telephone_numbers = []

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        incoming = text[0]
        outgoing = text[1]
        if incoming not in unique_telephone_numbers:
            unique_telephone_numbers.append(incoming)
        if outgoing not in unique_telephone_numbers:
            unique_telephone_numbers.append(outgoing)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        incoming = call[0]
        outgoing = call[1]
        if incoming not in unique_telephone_numbers:
            unique_telephone_numbers.append(incoming)
        if outgoing not in unique_telephone_numbers:
            unique_telephone_numbers.append(outgoing)

print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
