import sys


for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    
    
    key = key.split(',')
    
    license = key[1]
    medallion = key[0]
    
    print(license, end = '\t')
    print(medallion)



