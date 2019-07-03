arr= [10,20,20,10,10,30,50,10,20]
arr1=list(set(arr))

list1=[]
for i in arr1:
    list1.append(arr.count(i))
list2=[]
for j in list1:
    x=j//2
    list2.append(x)
print(sum(list2))



