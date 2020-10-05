import sys
from datetime import datetime
# input must be sorted
class Trips:
    def __init__(self):
        self.medallion = None
        self.dates = set()
        self.num_trips = 0
        

    
trips = Trips()
for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    
    medallion = key
    date, num_trips = val.split(',')
    num_trips = int(num_trips)
    
    
    if trips.medallion == None:
        trips.medallion = medallion
        trips.dates.add(date)
        trips.num_trips = num_trips # already an int
        
    # organized by medallion
    else:
        if trips.medallion == medallion:
            trips.num_trips += num_trips
            trips.dates.add(date)
            
        else:
            average_rides_per_day = trips.num_trips / len(trips.dates)
            
            
            print(trips.medallion, end = '\t')
            print(trips.num_trips, end = ',')
            print(average_rides_per_day)
            
            trips = Trips()
            trips.medallion = medallion
            trips.dates.add(date)
            trips.num_trips = num_trips
            
if trips.medallion != None:
    average_rides_per_day = float(trips.num_trips) / len(trips.dates)
    
    print(trips.medallion, end = '\t')
    print(trips.num_trips, end = ',')
    print(average_rides_per_day)
    
    
    
