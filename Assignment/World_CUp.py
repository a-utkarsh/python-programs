import time
import sys
tick=time.time()
print("")
t=(2019,5,30,15,0,0,1,48,0)
wc=time.mktime(t)

if (tick < wc):
    rm = wc - tick
    day = rm // (60 * 60 * 24)
    hrs = ((rm % (60 * 60 * 24)) // (60 * 60))
    mn = (((rm % (60 * 60 * 24)) % (60 * 60)) // 60)
    sc = (((rm % (60 * 60 * 24)) % (60 * 60)) % 60)
    day1 = int(day)
    hrs1 = int(hrs)
    mn1 = int(mn)
    sc1 = int(sc)
    while day1 > -1:
        while hrs1 > -1:
            while mn1 > -1:
                while sc1 > 0:
                    sc1 = sc1 - 1
                    time.sleep(1)
                    sys.stdout.write('\r' + "World Cup Start in : " + str(day1) + "Days " + str(hrs1) + "Hours " + str(mn1) + "Min " + str(sc1) + "Sec")

                mn1 = mn1 - 1
                sc1 = 60
            hrs1 = hrs1 - 1
            mn1 = 59
        day1 = day1 - 1
        hrs1 = 23

    print('Countdown Complete.')





