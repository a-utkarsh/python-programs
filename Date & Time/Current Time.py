import time;

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

'''

0 	tm_year 	2008
1 	tm_mon 	    1 to 12
2 	tm_mday 	1 to 31
3 	tm_hour 	0 to 23
4 	tm_min 	    0 to 59
5 	tm_sec 	    0 to 61 (60 or 61 are leap-seconds)
6 	tm_wday 	0 to 6 (0 is Monday)
7 	tm_yday 	1 to 366 (Julian day)
8 	tm_isdst 	-1, 0, 1, -1 means library determines DST

'''