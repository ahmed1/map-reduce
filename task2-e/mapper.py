import sys


for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    
    val = val.split(',')
    key = key.split(',')
    
    medallion = key[0]
    date = val[2][:10]
    
    print(medallion, end='\t')
    print(date, end = ',')
    print(1)
    
