"""A vaccination calculator."""

__author__ = "730225231"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses: int = int(input("Doses administered: "))
days = int(input("Doses per day: "))
percent: int = int(input("Target percent vaccinated: "))
need_vaccines: int = round(pop * (percent/100)* 2)
remainder: int = need_vaccines - doses
days_needed: int = round(remainder / days)
today: datetime = datetime.today()
end_date: timedelta = timedelta(days_needed)
final_date: datetime = today + end_date
print("We will reach " + str(percent) + "% vaccination in " + str(days_needed) + " days, which falls on " + final_date.strftime("%B %d, %Y") + ".")