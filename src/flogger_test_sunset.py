
import ephem
import datetime
import pytz

# 
# This module provides a function to test whether sunset time has passed
# given the coordinates of a location, normally the airfield for which flights are being logged.
# The local time is used and not UTC so should take into account Summer Time/Winter Time at the
# logging location
#
# 20190115

class init_sunset():
	def __init__(self, lat, lon, elv, USN_adj):	
		print "init check_sunset"
		self.dtnow      = ephem.Observer()
		self.dtnow.lon  = str(lon) 		#Note that lon should be in string format
		self.dtnow.lat  = str(lat)      	#Note that lat should be in string format
		self.dtnow.elev = elv
		#To get U.S. Naval Astronomical Almanac values, use these settings, USN_adj = -0.34 arcminutes
		self.dtnow.pressure= 0
		self.dtnow.horizon = str(USN_adj)
	def is_sun_set_now(self):
		self.dtnow.date = pytz.utc.localize(datetime.datetime.utcnow())	# Datetime Now
		self.sunset_nxt = self.dtnow.next_setting(ephem.Sun())					# Datetime next sunset Now
		self.nowdate = datetime.datetime.strptime(str(self.dtnow.date), "%Y/%m/%d %H:%M:%S").date()
		self.ssdate = datetime.datetime.strptime(str(self.sunset_nxt), "%Y/%m/%d %H:%M:%S").date()
		print "nowdate1 is: ", self.nowdate 
		print "ssdate1 is: ", self.ssdate
		if self.ssdate > self.nowdate:
			print "Sunset date for next day, hence sun has set for today"
			return True
		else:
			print "Sun has not set yet for today: ", self.nowdate
			return False
			
#check = init_sunset(54.2289592, -1.20928758608, 238.25, "-0:34")
#issunset = check.is_sun_set_now()
#print "Is sun set now?: ", issunset
		
		
		
		
	
		


