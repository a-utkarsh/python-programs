list1=[27, 5, 2, 25]
for i in range(len(list1)):
    next=-1
    for j in range(i+1,len(list1)):
        if list1[j]>list1[i]:
            next=list1[j]
            break
    print(str(list1[i]), "---" ,next)
