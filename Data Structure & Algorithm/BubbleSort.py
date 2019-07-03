def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]

    return list
list1=[]
n=int(input("Enter number of element in list"))
for i in range(n):
    num = int(input("Enter number to list"))
    list1.append(num)
print(bubbleSort(list1))

