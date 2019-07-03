s="12:05:45AM"

time=s.split(":")
if(int(time[0])==12 and time[2].__contains__("PM")):
    c = time[2].strip("PM")
    print(str(int(time[0])) + ":" + time[1] + ":" + str(c))
elif(int(time[0])==12 and time[2].__contains__("AM")):
    c = time[2].strip("PM")
    print("00" + ":" + time[1] + ":" + str(c))


elif time[2].__contains__("PM"):
    c=time[2].strip("PM")
    print(str(12+int(time[0]))+":"+time[1]+":"+str(c))


else:
    c = time[2].strip("AM")
    print(str((time[0])) + ":" + time[1] + ":" + str(c))

