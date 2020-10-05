"""
a) Find the distribution of fare amounts (fare_amount) for each of the following ranges: [0, 20],
[20.01, 40], [40.01, 60], [60.01, 80], [80.01, infinite],
Thus, for each range, give the number of trips whose fare amount falls in that range.
Output: A key-value pair per line, where the key is the range, and the value is the number of trips. For example,
0,20 100 20.01,40 300 ...
    2
The output directory must be named FareAmounts.
"""
import sys


for line in sys.stdin:

    line = line.strip()
    
    key, val = line.split('\t')
    
    val = val.split(',')
    
    
    # -6 is the fare thing
    fare_amount = val[-6]

    fare_amount = float(fare_amount)
    if fare_amount >= 0 and fare_amount <= 20:
        print('0, 20\t', 1)
    
    elif fare_amount >= 20.01 and fare_amount <= 40:
        print('20.01, 40\t', 1)
    
    elif fare_amount >= 40.01 and fare_amount <= 60:
        print('40.01, 60\t', 1)
    elif fare_amount >= 60.01 and fare_amount <= 80:
        print('60.01, 80\t', 1)
    elif fare_amount >= 80.01 :
        print('80.01, infinite\t', 1)
    else:
        pass
