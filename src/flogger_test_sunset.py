
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
#	def __init__(self, lat, lon, elv, USN_adj):	
	def __init__(self, location):
		print "init check_sunset"
		self.sun = ephem.Sun()
		self.twilight = -6 & ephem.degree
		
	def is_sunset_now(self, settings, location): 
		log_datetime = datetime.datetime.now() + datetime.timedelta(hours=int(settings.FLOGGER_LOG_TIME_DELTA))
		location.date = ephem.Date(log_datetime)
		print "Ephem date is: ", location.date
		s = ephem.Sun()
		s.compute(location)
		twilight = -6 * ephem.degree    # Defn of Twilight is: Centre of Sun is 6, 12, 18 degrees below horizon (civil, nautical, astronomical)  
		if s.alt > twilight:
			print "Is it light at Location? Yes", location, \
			" Ephem date is: ", ephem.Date(location.date), \
			" Next sunset at: ", location.next_setting(ephem.Sun())
			return True
		else:
			print "Is it light at Location? No", location, \
			" Ephem date is: ", ephem.Date(location.date), \
			" Next sunrise at: ", location.next_rising(ephem.Sun())
			return False
            
                
		
		
#		nowdate     = ephem.localtime(self.dtnow.date)
#		sunrise_nxt = ephem.localtime(self.dtnow.previous_rising(ephem.Sun()))
#		sunset_nxt  = ephem.localtime(self.dtnow.next_setting(ephem.Sun()))
#		print "nowdate is: ", nowdate
#		print "sunrise_nxt is: ", sunrise_nxt
#		print "sunset_nxt is: ", sunset_nxt
#		if (nowdate > sunrise_nxt) and (nowdate < sunset_nxt):
#			return False
#		else:
		#	print False
#			return True
			
#check = init_sunset(54.2289592, -1.20928758608, 238.25, "-0:34")
#issunset = check.is_sun_set_now()
#print "Is sun set now?: ", issunset
		
		
		
		
	
		


