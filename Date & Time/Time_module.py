import time

print ("time.altzone %d " % time.altzone)

#asctime
t = time.localtime()
print ("time.asctime(t): %s " % time.asctime(t))
print(time.clock())
#The following example shows the usage of clock() method.

import time

def procedure():
   time.sleep(3)

# measure process time
t0 = time.clock()
procedure()
print (time.clock(), "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")
print("")

#ctime
print ("time.ctime() : %s" % time.ctime())
print(time.gmtime())

#strftime
import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
print("")
t = time.mktime(t)
print("")
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

#sleep

print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())

#strptime
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print ("returned tuple:" ,struct_time)