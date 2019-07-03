#Write a Python program to print the calendar of a given month and year.
import calendar
year = int(input("Input the year : "))
month = int(input("Input the month : "))
print(calendar.month(year,month))

print(calendar.isleap(year))

print(calendar.calendar(year))
print(calendar.leapdays(1918,2018))
print(calendar.monthrange(year , month))
print(calendar.monthcalendar(year, month))
print(calendar.weekday(1996, 11, 19))
list1=[]
for i  in calendar.day_name:
    list1.append(i.upper())
print(list1)


