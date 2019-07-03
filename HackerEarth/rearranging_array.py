arr=[3,5,3,5,5,11,5]
x=5
result=[]
for i in range(len(arr)):
    if arr[i]!=x:
        result.append(arr[i])
    #for j in range(flag):
    #    arr[j]=1
for i in range(len(arr)-len(result)):
    result.insert(i,1)
print(result)
