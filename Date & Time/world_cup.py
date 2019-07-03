import time
import sys
def GetTime(time):
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    sys.stdout.write('\r' + "Cricket World Cup Start in : " + str(int(day)) + "Days " + str(int(hour)) + "Hours " + str(int(minutes)) + "Min " + str(int(seconds)) + "Sec")

while True:
    today = time.time()
    date_str = "2019-05-30 15:00:00"
    time_tuple = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    match = time.mktime(time_tuple)
    timeremain = match- today
    time.sleep(1)
    GetTime(timeremain)
