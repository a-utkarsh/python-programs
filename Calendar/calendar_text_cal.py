import calendar

c= calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2018,7)
print(str)

print("")
c= calendar.TextCalendar(calendar.THURSDAY)
str = c.formatmonth(2018,7)
print(str)