arr=[9,8,7,4,5,2,0,1,3,6]
gap=len(arr)//2
while gap>0:
    for i in range(gap,len(arr)):
        temp=arr[i]
        j=i
        while j>=gap and arr[j-gap]>temp:
            arr[j]=arr[j-gap]
            j-=gap

        arr[j]=temp
    gap//=2
print(arr)
