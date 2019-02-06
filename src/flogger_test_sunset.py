
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
		self.sunset_time = location.next_setting(ephem.Sun())
		self.sunrise_time = location.previous_rising(ephem.Sun())
		
		self.sunset_datetime = self.sunset_time.datetime()
		self.sunrise_datetime = self.sunrise_time.datetime()
		# Find sunset day
		self.sunset_datetime = datetime.datetime.strptime(str(self.sunset_time.datetime()), "%Y-%m-%d %H:%M:%S.%f")
		self.sunset_day = self.sunset_datetime.date()
		# Find sunrise day
		self.sunrise_datetime = datetime.datetime.strptime(str(self.sunrise_time.datetime()), "%Y-%m-%d %H:%M:%S.%f")
		self.sunrise_day = self.sunrise_datetime.date()
		return
	
	def is_sunset_now(self, location): 
		print "In is_sunset_now function"  
		datetime_now = datetime.datetime.now() 
		datetime_day = datetime_now.date()
		#print "Datetime_now: ", datetime_now.date()
		print "Current daytime is: ", datetime_now, \
		" Sunset_day is: ", self.sunset_day, \
		" Sunset time is: ", self.sunset_datetime, \
		" Sunrise day is: ", self.sunrise_day
		if self.sunrise_day == datetime_day and self.sunset_day == datetime_day:
			# Sunrise and sunset on same day
			if datetime_now < self.sunset_datetime:
				#print "Sun not set"
				return False
			else:
				#print "Sun is set"
				return True
		else:
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
		

		
		
	
		


