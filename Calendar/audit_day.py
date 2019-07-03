import calendar

for month in range(1, 13):
# It retrieves a list of weeks that represent the month
        mycal = calendar.monthcalendar(2018, month)
# The second MONDAY has to be within the first two weeks
        week1 = mycal[1]
        week2 = mycal[2]
        if week1[calendar.MONDAY] != 0:
            auditday = week1[calendar.MONDAY]
        else:
             # if the second MONDAY isn't in the first week,
             #  it must be in the second week
            auditday = week2[calendar.MONDAY]
        print("%10s %2d" % (calendar.month_name[month], auditday))
'''mycal = calendar.monthcalendar(2025, month) will create calendar for the 
month
Set variables week1 and week2 to the First and second week of the calendar
Check if Week 1 contains Monday, set audit day
Else set audit day as the first Monday in week 2
The output shows the date for the first Monday that falls in that month. '''