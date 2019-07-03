#code
arr=[10,3,7,4,2,6,5,10,9]
low=-1
mid=0
high=1
result=[]
while mid<len(arr) and low<len(arr)-1 and high<len(arr):
    if(mid==0) and (arr[high]>arr[mid]):
        result.append(arr[mid])
    elif(arr[low]>arr[mid]<arr[high]):
        result.append(arr[mid])
    elif(high==len(arr)-1 and arr[mid]>arr[high]):
        result.append(arr[high])

    low += 1
    high += 1
    mid += 1
print(result)