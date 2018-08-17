#!/usr/bin/python3
from pysolar.solar import *
import datetime

# your location (Example Romalt in Denmark, 0 meters above sealevel)
lat = 56.4444472
lon = 10.0838776
eve = 0

# Time section
# Use now or specific time
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
# get_altitude is given 3 parameters :
#   lat - Latitude
#   lon - Longitude
#   eve - Evelation

print("Altitude : " , get_altitude(lat, lon, date, eve))
print("Azimuth  : ", -1 * get_azimuth(lat, lon, date) + 180)

