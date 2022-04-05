import datetime
from fileStorage import storeArray

from getInput import *

period = ["9:00","10:00","11:15","13:15","14:15"]
# Base timetable
timetable = [
    ["Science","Maths","English","PE","Special"],
    ["Culture","Maths","Science","English","PE"],
    ["English","Maths","PE","Science","Culture"],
    ["PE","Maths","Culture","Science","English"],
    ["Special","Maths","English","PE","Science"]
]

def displayTimetable(tt):
    print("Todays timetable:")
    for x in range(len(tt)):
        print("    Period {0}: {1}".format(x+1, tt[x]))

def fetchTimetable():
    d = datetime.date.today()
    todays_schedule = timetable[d.weekday()]
    return todays_schedule

def nextPeriod(time):
    splitstring = time.split(":")
    hour = int(splitstring[0])
    minute = int(splitstring[1])
    t = datetime.time(hour,minute)
    d = datetime.now()
    
def createFilename(type, general, specific):
    # type of variable
    # what is generally about it
    # what is specific about it
    return (general + "_" + specific + "." + type)

filename = createFilename("array", "period", "times")
check = storeArray(period, filename)

filename = createFilename("array", "timetable", "monday")
check = storeArray(timetable[0], filename)

d=0
