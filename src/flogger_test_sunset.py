
import ephem
import datetime
#import pytz
#from datetime import datetime
#import ephem

# 
# This module provides a function to test whether sunset time has passed
# given the coordinates of a location, normally the airfield for which flights are being logged.
# The local time is used and not UTC so should take into account Summer Time/Winter Time at the
# logging location
#
# 20190119

class init_sunset_test():	
	def __init__(self, location):	
		#print "init check_sunset"
		#self.sun = ephem.Sun()
		self.twilight = -6 * ephem.degree
		self.sunset_time = location.next_setting(ephem.Sun())
		
		self.sunset_datetime = self.sunset_time.datetime()
		#print "Sunset as datetime: ", self.sunset_time.datetime()
		# Find sunset day
		self.sunset_datetime = datetime.datetime.strptime(str(self.sunset_time.datetime()), "%Y-%m-%d %H:%M:%S.%f")
		self.sunset_day = self.sunset_datetime.date()
		#print "init sunset_day: ", self.sunset_day
		return
	
	def is_sunset_now(self, location): 
		print "In is_sunset_now function"  
		datetime_now = datetime.datetime.now()
		#print "Datetime_now: ", datetime_now.date()
		print "Current day is: ", datetime_now.date(), " Sunset_day is: ", self.sunset_day, " Sunset time is: ", self.sunset_datetime
		if self.sunset_day > datetime_now.date():
			print "Sunset day is tomorrow, must be set today"
			return True
		if datetime_now < self.sunset_datetime:
			print "Sun not set"
			return False
		else:
			print "Sun is set"
			return True

#location = ephem.Observer()        
#location.lat = str(54.2289592)
#location.lon = str(-1.20928758608)
#location.elevation = 238.25
			
#check = init_sunset_test(location)
#check.init_sunset(location)
#print "Check: ", check
#issunset = check.is_sunset_now(location)
#print "Is sun set now?: ", issunset
		

		
		
	
		


