import sys

dist_one = 0
dist_two = 0
dist_three = 0
dist_four = 0
dist_five = 0

for line in sys.stdin:


    line = line.strip()
    
    key, val = line.split('\t')
    
    if key == '0, 20':
        dist_one +=1
    elif key == '20.01, 40':

        dist_two +=1
        
    elif key == '40.01, 60':
        dist_three +=1
        
    elif key == '40.01, 80':
        dist_four +=1
        
        
    elif key == '80.01, infinite':
        dist_five +=1
        
print('0, 20\t', dist_one)
print('20.01, 40\t', dist_two)
print('40.01, 60\t', dist_three)
print('60.01, 80\t', dist_four)
print('80.01, infinite\t', dist_five)
