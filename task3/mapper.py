import sys



for line in sys.stdin:
    line = line.strip()
    
    if '\t' not in line:
    
        splits = line.split(',')
    
        if splits[0] == 'medallion':
            pass
        else:
            
            medallion = splits[0]
            
            
            print(medallion, end = '\t')
            
            for idx in range(1, len(splits) - 1):
                print(splits[idx], end = ',')
            print(splits[-1])
        
                
                
    else:
        key, val = line.split('\t')
        
        key = key.split(',')
        val = val.split(',')
        
        medallion = key[0]
        
        print(medallion, end = '\t')
        
        for idx in range(1, len(key)):
            print(key[idx], end = ',')

        for idx in range(1, len(val)-1):
            print(val[idx], end = ',')
        print(val[-1])

