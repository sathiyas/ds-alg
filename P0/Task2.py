"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

duration = {}

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        incoming = call[0]
        outgoing = call[1]
        call_time = int(call[3])
        if incoming in duration:
            total_time = int(duration[incoming])
            total_time += call_time
            duration[incoming] = total_time
        else:
            duration[incoming] = call_time
        if outgoing in duration:
            total_time = int(duration[outgoing])
            total_time += call_time
            duration[outgoing] = total_time
        else:
            duration[outgoing] = call_time
max_key = None
max_value = 0
for key in duration.keys():
    if duration[key] > max_value:
        max_key = key
        max_value = duration[key]
print(f"{max_key} spent the longest time, {max_value} seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

