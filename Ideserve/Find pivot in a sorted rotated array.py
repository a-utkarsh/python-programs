'''
Ex=[78,82,99,10,23,35,49,51,60]
pivot element is the smallest element
'''
#Algorithm 1:Travers the complete array
arr=[78,82,99,10,23,35,49,51,65]
pivot=-1
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        pivot=i+1
        break
print(pivot)

#Algorithm 2:using binary search
if arr[0]<=arr[len(arr)-1]:
    print("array not sorted")
start=0
end=len(arr)-1
piv=-1
while start<=end:
    mid=(start+end)//2
    if arr[mid] > arr[mid + 1]:
        piv=mid+1
    if arr[start]<=arr[mid]:
        start=mid+1
    else:
        end=mid-1
print(piv)

