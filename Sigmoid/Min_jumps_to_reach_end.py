def jumps(arr):
    if len(arr)<=1:
        return 0
    ladder=arr[0]
    stairs=arr[0]
    jump=1
    for level in range(1,len(arr)-1):
        if(level==len(arr)-1):
            return jump
        if(level+arr[level]>ladder):
            ladder=level+arr[level]
        else:
            stairs-=1
        if(stairs==0):
            jump+=1
            stairs=arr[level]
    return jump
arr=[1, 3, 6, 1, 0, 9]
print(jumps(arr))