import sys


for line in sys.stdin:

    line = line.strip()
    
    key, val = line.split('\t')
    val = val.split(',')
    
    date = val[2][:10]
    total_amount = val[-1]
    tip_amount = val[-3]
    
    print(date, end = '\t') # key
    print(total_amount, ',', tip_amount) # value
    
