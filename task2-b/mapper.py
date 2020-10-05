import sys


for line in sys.stdin:


    line = line.strip()
    
    key, val = line.split('\t')
    val = val.split(',')
    
    total_amount = val[-1]
    
    
    print(total_amount, end = '\t') # just to allow to split
    print(1)
