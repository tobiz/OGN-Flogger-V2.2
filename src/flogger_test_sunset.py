
import ephem
#from ephem import *
import datetime
import pytz

# 
# This module provides a function to test whether sunset time has passed
# given the coordinates of a location, normally the airfield for which flights are being logged.
# The local time is used and not UTC so should take into account Summer Time/Winter Time at the
# logging location
#
# 20190119

#class init_sunset(self):
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
		
	def is_sunset_now(self): 
		nowdate     = ephem.localtime(self.dtnow.date)
		sunrise_nxt = ephem.localtime(self.dtnow.previous_rising(ephem.Sun()))
		sunset_nxt  = ephem.localtime(self.dtnow.next_setting(ephem.Sun()))
		print "nowdate is: ", nowdate
		print "sunrise_nxt is: ", sunrise_nxt
		print "sunset_nxt is: ", sunset_nxt
		if (nowdate > sunrise_nxt) and (nowdate < sunset_nxt):
			return False
		else:
		#	print False
			return True
			
#check = init_sunset(54.2289592, -1.20928758608, 238.25, "-0:34")
#issunset = check.is_sun_set_now()
#print "Is sun set now?: ", issunset
		
		
		
		
	
		


