# http://www.pythonchallenge.com/pc/return/uzi.html
import calendar
from datetime import date

years = [y for y in range(1006, 2006, 10) if calendar.isleap(y) and date(y, 1, 1).isoweekday() == 4]
print date(years[-2], 1, 27)
