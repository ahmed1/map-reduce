import sys


for line in sys.stdin:
    
    
    # passenger count is val[3]
    line = line.strip()
    
    key, val = line.split('\t')
    
    val = val.split(',')
    passenger_count = val[3]
    
    print(passenger_count, end = '\t')
    print(1)

