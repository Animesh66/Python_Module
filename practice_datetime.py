import time
from datetime import datetime

dt = datetime(year=2018, month=12, day=21)
converted = dt.strftime("%Y/%m")
print(datetime.strptime("01/01/2022", "%d/%m/%Y"))
print(type(converted))