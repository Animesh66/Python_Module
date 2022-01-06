from datetime import datetime
from time import time

epic_time = time()  # returns the time from origin of OS
print(epic_time)
print("No of Years: ", epic_time/31536000)
dt = datetime.now()  # returns the current timestamp
print(dt)
print(dt.strftime("%Y/%m/%d"))  # strftime conversts date to string format
print(datetime.strptime("2018-12-01", "%Y-%m-%d"))  # strptime converts string to date format
