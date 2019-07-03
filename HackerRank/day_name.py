import calendar
list1=[]
for i  in calendar.day_name:
    list1.append(i.upper())
month, day ,year= map(int, input().split())

print(calendar.day_name[calendar.weekday(year, month, day)].upper())