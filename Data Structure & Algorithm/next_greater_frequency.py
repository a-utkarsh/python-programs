list1=[1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
count=[]
result=[]
for item in (list1):
    count.append(list1.count(item))
print(list1)
for i in range(len(count)):
    next=-1
    for j in range(i+1,len(count)):
        if count[j]>count[i]:
            next=count[j]
            break
    if next!=-1:
        result.append(list1[count.index(next)])
    else:
        result.append(-1)
print(result)


