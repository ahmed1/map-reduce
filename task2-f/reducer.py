import sys
class Driver:
    def __init__(self):
        self.license = None
        self.medallions = set()
driver = Driver()
for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    license = key
    medallion = val
    
    if driver.license == None:
    
        driver.license = license
        driver.medallions.add(medallion)
    else:
        if driver.license == license:
            driver.medallions.add(medallion)
        
        else:
            print(driver.license, end = '\t')
            print(len(driver.medallions))
            
            driver = Driver()
            driver.license = license
            driver.medallions.add(medallion)
            
            
if driver.license != None:
    print(driver.license, end = '\t')
    print(len(driver.medallions))
