import sys

num_trips = 0
for line in sys.stdin:

    line = line.strip()
    
    key, val = line.split('\t')
    
    if float(key) <= 15:
        num_trips +=1
print(num_trips)

