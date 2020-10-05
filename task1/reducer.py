"""
Case 1
key is empty -> add to key , val

Case 2
Key has value
    Case1
        new key == old key
        append new vals
    Case 2
        new key != old key
        Case1
            if len(val) == 1:
                do nothing
        Case 2
            if len(val) > 1:
                sort val by descending (trips is first and has more values)
                flatten val
                print it
                

"""
class Join:
    def __init__(self):
        self.key = ''
        self.left_val = []
        self.right_val = []
        self.left_val_len = 10 # some interesting stuff here
        self.right_val_len = 7
    def reset(self):
        self.key = ''
        self.left_val = []
        self.right_val = []
        


    
def print_row(key, left_val, right_val):
    
    print(key, end = '\t')
    
    
    print(left_val, end = ',')
    print(right_val)
    
    
import sys
count = 0
joins = Join()

for line in sys.stdin:
    
    line = line.strip()
    
    key, val = line.split('\t')


    val_len = len(val.split(','))


    

    
    if joins.key == '':
        joins.key = key

        
        if val_len == joins.left_val_len:
            
            joins.left_val.append(val)
        elif val_len == joins.right_val_len:
            joins.right_val.append(val)
            

        else:
            print(len(val), val)
            print('SOMETHING IS BROKEN!!!')

        
    else:
        if joins.key == key:
            
            if val_len == joins.left_val_len:
                
                joins.left_val.append(val)
            elif val_len == joins.right_val_len:
                joins.right_val.append(val)

            else:
                pass

        else:
             
            if (joins.left_val and not joins.right_val) or (not joins.left_val and joins.right_val):
                joins.reset()
        
            else:
                

                joins.left_val = list(set(joins.left_val))
                joins.right_val = list(set(joins.right_val))
                

                for i in range(len(joins.left_val)):
                    for j in range(len(joins.right_val)):
                        print_row(joins.key, joins.left_val[i], joins.right_val[j])
#                print('DONE PRINTING')
#                sys.exit()
        
        
            joins.reset()
            joins.key = key
            
            if val_len == joins.left_val_len:
                joins.left_val.append(val)
            elif val_len == joins.right_val_len:
                joins.right_val.append(val)
            
