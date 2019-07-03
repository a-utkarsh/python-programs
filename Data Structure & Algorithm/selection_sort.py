arr=[3,4,2,1,7,6,9,8,0]
for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j

    arr[i], arr[min_idx]=arr[min_idx],arr[i]
print(arr)

