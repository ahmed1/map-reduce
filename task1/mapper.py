import sys

for line in sys.stdin:
   
        
         
    line = line.strip()
#        print(line)
    splits = line.split(',')
    if splits[0] == 'medallion':
        pass
    else:
        if len(splits) == 14: # trips file (not normal)
    #            print('here')
            
            medallion = splits[0]
            hack_license = splits[1]
            vendor_id = splits[2]
            pickup_datetime = splits[5][:16] # only for samp
            
            # append 0 to first key
#            print('0', end = '')
            print(medallion, end = ',')
            print(hack_license, end = ',')
            print(vendor_id, end = ',')
            print(pickup_datetime, end = '\t')
            
            print(splits[3], end = ',')
            print(splits[4], end = ',')
            
            
            
            for idx in range(6, len(splits)-1):
                print(splits[idx], end = ',')
            print(splits[-1])
        elif len(splits) == 11: # fares file
        
            medallion = splits[0]
            hack_license = splits[1]
            vendor_id = splits[2]
            pickup_datetime = splits[3]
            
            print(medallion, end = ',')
            print(hack_license, end = ',')
            print(vendor_id, end = ',')
            print(pickup_datetime, end = '\t')
            
            
            for idx in range(4, len(splits)-1):
                print(splits[idx], end = ',')
            
            print(splits[-1])
        else:
            print(len(splits), splits)
            print('YOUR PROGRAM BROKE')
            pass
    #            sys.exit()
        
        
