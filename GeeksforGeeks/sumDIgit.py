def sumx(N):

    list1=list(str(N))
    list2=[]
    for i in list1:
        list2.append(int(i))
    sum1= list2[0]+list2[len(list2)-1]
    sum2=0
    for i in range(1,len(list2)-1):
        sum2= sum2+list2[i]
    if sum1==sum2:
        return "YES"
    else:
        return "NO"
T=int(input())
number=[]
result=[]
for i in range(T):
    num=int(input())
    number.append(num)
for j in number:
    result.append(sumx(j))
for i in result:
    print(i)
