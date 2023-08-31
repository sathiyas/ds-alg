"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

telemarketers = []
text_recievers = []
text_senders = []
call_recivers = []


with open('texts.csv', 'r') as f:
    """
    Build list of text senders and recievers
    """
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        sender = text[0]
        reciever = text[1]
        if sender not in text_senders:
            text_senders.append(sender)
        if reciever not in text_recievers:
            text_recievers.append(reciever)

with open('calls.csv', 'r') as f:
    """
    Build list of call recievers
    """
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        calling = call[0]
        recieving = call[1]
        if recieving not in call_recivers:
            call_recivers.append(recieving)
    for call in calls:
        outgoing = call[0]
        if outgoing not in text_recievers and outgoing not in text_recievers and outgoing not in call_recivers:
            if outgoing not in telemarketers:
                telemarketers.append(outgoing)

telemarketers.sort()

print("These numbers could be telemarketers: ")
for x in telemarketers:
    print(x)
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

