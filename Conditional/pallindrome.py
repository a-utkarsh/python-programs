N =int(input())
list1=[]
for i in range(N):
    temp=i
    rev=0
    while(i>0):
        dig=i%10
        rev=rev*10+dig
        i=i//10
    if(temp==rev):
        list1.append(temp)
print(list1)
