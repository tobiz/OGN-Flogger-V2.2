#
# This dumps the flights table to a csv file.  The file name is "todays_date_time"_flights.csv
#
import flogger_settings
import string
import datetime
import time
import sqlite3
import pytz
from datetime import timedelta
import csv
import os
from flogger_path_join import *
   
#
# See http://stackoverflow.com/questions/17556450/sqlite3-python-export-from-sqlite-to-csv-text-file-does-not-exceed-20k
#

def dump_flights(settings):  
    #    
    #-----------------------------------------------------------------
    # This function converts and dumps todays' flights
    # as a csv file.  If there are no flight records in flights table
    # it exists without creating a csv file.
    #-----------------------------------------------------------------
    #
    path = os.path.dirname(os.path.abspath(__file__))
#    db_file = os.path.join(path,"../db/" + settings.FLOGGER_DB_NAME)
    db_name = str(settings.FLOGGER_DB_NAME)
#    db_file = path_join_dd(os.path.abspath(__file__), ["db", settings.FLOGGER_DB_NAME])
    db_file = path_join_dd(os.path.abspath(__file__), ["db", db_name])
#    flight_log_file = os.path.join(path,"../logs/" + settings.FLOGGER_FLIGHTS_LOG)
    flights_log = str(settings.FLOGGER_FLIGHTS_LOG)
#    print "flights_log is: ", flights_log
#   flight_log_file = path_join_dd(os.path.abspath(__file__), ["logs", settings.FLOGGER_FLIGHTS_LOG])
#    flights_log_file = path_join_dd(os.path.abspath(__file__), ["logs", flights_log])
#    flights_log_file = path_join_dd(os.path.abspath(__file__), ["logs", flights_log])
    flights_log_file_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )), "logs")
    if not os.path.exists(flights_log_file_path):
        os.mkdir(flights_log_file_path)
        print "Directory created: " , flights_log_file_path 
    else:    
        print "Directory already exists: " , flights_log_file_path

#    flights_log_file = os.path.join(flights_log_file_path, flights_log)
    flights_log_file = flights_log_file_path
#    print "flight_log file path name is: ", flights_log
    
    print "Start flights table dump"
    try:
#        db = sqlite3.connect(settings.FLOGGER_DB_NAME)
        db = sqlite3.connect(db_file)
        #Get a cursor object
        cursor = db.cursor()
    except:
        print "Failed to connect to db"
        
    try:
        cursor.execute('''SELECT max(sdate) FROM flights''')
        max_row = cursor.fetchone()
    except:
        print "failed to select max(sdate) FROM flights"
        
    start_time = str(datetime.datetime.now()).replace(" ", "_")
    # Make a unique filename
#   csv_path = settings.FLOGGER_FLIGHTS_LOG + start_time + "_flights.csv"
#    csv_path = flights_log_file + start_time + "_flights.csv"
#    csv_path = os.path.join(flights_log_file, (start_time + "_flights.csv"))
    flights_file_name = (start_time + "_flights.csv").replace(":", "-") #This for Windows files
    csv_path = os.path.join(flights_log_file, flights_file_name)
    print "csv file name is: ", csv_path  
    
    if max_row <> (None,): 
        max_date = "".join(max_row[0:3])        #max_row[0:3] is sdate
        print "Dump flights to csv. Last record date in flights is: ", max_date
#         cursor.execute("SELECT * FROM flights WHERE sdate=? ORDER by sdate, stime", (max_date,))
        cursor.execute("SELECT flight_no, sdate, stime, etime, duration, src_callsign, max_altitude, registration, track_file_name, tug_registration, tug_altitude, tug_model  FROM flights WHERE sdate=? ORDER by sdate, stime", (max_date,))       

        with open(csv_path, "a+") as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write headers.
            print "Output header"
            csv_writer.writerow([i[0] for i in cursor.description])
            # Write data.
            print "Output data"
            csv_writer.writerows(cursor)
        csv_file.close()
#        print "End flights table dump"
#        return
    else:
        print "No records in flights so set date to today"
        today = datetime.date.today().strftime("%y/%m/%d")
        max_date = datetime.datetime.strptime(today, "%y/%m/%d")
        print "max_date is: ", max_date
#        csv_file = open(csv_path, "w+b")
        csv_file = open(csv_path, "w+")
        csv_file.truncate(0)        # Zero length the file
        csv_file.close()
#        return
    
    print "End flights table dump"
    return csv_path

    
    
