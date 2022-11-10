from datetime import date, time, datetime, timedelta
import re

today = date.today()
print("output #41:today:{0!s}".format(today))
print("output #42:{0!s}".format(today.year))
current_datetime = datetime.today()
print (current_datetime)

eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))