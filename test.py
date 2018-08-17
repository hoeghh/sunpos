#!/usr/bin/python3
from pysolar.solar import *
import datetime

# your location (Example Romalt in Denmark)
lat = 56.4444472
lon = 10.0838776

# Time section
# Use now or specifi time
#
# Now :
#   date = datetime.datetime.now()
#
# Specific : 
#   date = datetime.datetime(2018, 8, 17, 20, 32, 51, 442391, tzinfo=datetime.timezone.utc)
#   Eg. 2018-08-17 20:32:51.442391
#   (Year, Month, Day, Hour, Minute, Second, Millisecond)

date = datetime.datetime.now()
print("Datetime : ", date)

# As Pysolar uses south as Zero with west as negative and east as positive
# we multiply with -1 and adds 180 to recalibrate to North as our point of zero
# http://docs.pysolar.org/en/latest/#examples
print("Altitude : " , get_altitude(lat, lon, date))
print("Azimuth  : ", -1 * get_azimuth(lat, lon, date) + 180)
