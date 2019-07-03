n=int(input())
arr = list(map(int, input().split()))[:n]
s=0
list1=[]
for i in range(len(arr)):
    x=sum(arr[i:len(arr)-1])
    list1.append(x)


print(max(list1))