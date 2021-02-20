# Exercise 1: Import ​datetime, time​ and ​calendar​ modules
import datetime
import time
import calendar

# Exercise 2: Print on separate lines՝:
# Exercise 2 a: The date of your birthday
my_birthdate=datetime.date(1997, 10, 13)
print("The date of my birthdate is", my_birthdate)

# Exercise 2 b: The year of your birthday (using the appropriate 
#				function on the date of your birthday)

birthdate_year = my_birthdate.year
print("The year of my birthdate is", birthdate_year)

# Exercise 2 c: The month of your birthday (using the appropriate 
# 				function on the date of your birthday)

birthdate_month = my_birthdate.month
print("The month of my birthdate is", birthdate_month)

# Exercise 2 d: The day of your birthday (using the appropriate 
#				function on the date of your birthday)

birthdate_day = my_birthdate.day
print("The day of my birthdate is", birthdate_day)

# Exercise 2 e: Find and print the weekday of your birthday

birthdate_weekday = my_birthdate.isoweekday()
print("The weekday of my birthdate is", birthdate_weekday)

# Exercise 2 f: Find and print how many days are left 
# 				till your upcoming birthday

next_birthdate = my_birthdate + datetime.timedelta(days = 365*24, hours = 24*6)
today = datetime.date.today()
till_birthday = next_birthdate - today
print("Days until my next birthday: ", till_birthday)

# Exercise 3: Print the calendar of May 2017 
may_2017_calendar = calendar.month(2017, 5)
print("Calendar of 2017 of May", '\n', may_2017_calendar)

# Exercise 4: Print yesterday’s date and time
one_day = datetime.timedelta(days = 1)
yesterday = datetime.datetime.today() - one_day
print("Yesterday was:", yesterday)

# Exercise 4 a: Add 2 days to yesterday’s date and time and print the result

two_days = datetime.timedelta(days = 2)
tomorrow = yesterday + two_days
print("Tomorrow will be", tomorrow)

# Exercise 4 b: Subtract 3 days from yesterday’s date 
#				and time and print the result

three_days = datetime.timedelta(days = 3)
three_day_before_yesterday = yesterday - three_days
print("Three days fefore yesteday was", three_day_before_yesterday)
