# needs to be sorted
import sys

class Passengers:
    def __init__(self):
        self.current_passenger_count = None
        self.num_trips = 0
passengers = Passengers()

for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    
    if passengers.current_passenger_count == None:
        passengers.current_passenger_count = key
        passengers.num_trips = float(val)
        
    else:
        if passengers.current_passenger_count == key:
            passengers.num_trips += float(val)
            
        else:
            print(passengers.current_passenger_count, end = '\t')
            print(int(passengers.num_trips))
            
            passengers = Passengers()
            passengers.current_passenger_count = key
            passengers.num_trips = float(val)
            
if passengers.current_passenger_count != None:
    print(passengers.current_passenger_count, end = '\t')
    print(int(passengers.num_trips))
