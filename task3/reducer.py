import sys

# sorted

class Join:
    def __init__(self):
        self.key = '' # medallion
        self.left_val = []
        self.right_val = []
        self.left_val_len = 19 # task1 output
        self.right_val_len = 15
    def reset(self):
        self.key = ''
        self.left_val = []
        self.right_val = []


def print_row(key, left_val, right_val):
    
    print(key, end = '\t')
    
    
    print(left_val, end = ',')
    print(right_val)
    
joins = Join()
for line in sys.stdin:

    line = line.strip()
    
    key, val = line.split('\t')
#    val = val.split(',')
    
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

if joins.left_val and joins.right_val:
    for i in range(len(joins.left_val)):
        for j in range(len(joins.right_val)):
            print_row(joins.key, joins.left_val[i], joins.right_val[j])
