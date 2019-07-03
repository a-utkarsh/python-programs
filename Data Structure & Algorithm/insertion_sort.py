list1=[2,1,3,5,4,0,6]
for i in range(1, len(list1)):
    j=i-1
    key=list1[i]
    while j>=0 and list1[j]>key:
        list1[j+1]=list1[j]
        j-=1
    list1[j+1]=key
    print(list1)
print(list1)
