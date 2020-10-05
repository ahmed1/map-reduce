import sys

# sorted by key
class TotalRevenue:
    def __init__(self):
        self.date = None
        self.total_amount = 0
        self.total_tips = 0
        
revenue = TotalRevenue()

for line in sys.stdin:

    line = line.strip()
    key, val = line.split('\t')
    
    amount, tips = val.split(',')
    
    if revenue.date == None:
        revenue.date = key
        revenue.total_amount = float(amount)
        revenue.total_tips = float(tips)
        
    else:
        if revenue.date == key:
            revenue.total_amount += float(amount)
            revenue.total_tips += float(tips)
        else:
            print(revenue.date, end = '\t')
            print(revenue.total_amount, end = ',')
            print(revenue.total_tips)
            
            revenue = TotalRevenue()
            revenue.date = key
            revenue.total_amount = float(amount)
            revenue.total_tips = float(tips)
            
if revenue.date != None:
    print(revenue.date, end = '\t')
    print(revenue.total_amount, end = ',')
    print(revenue.total_tips)
