arr=[9,8,4,5,1,3,6]
my_max=max(arr)
my_min=min(arr)
size= my_max-my_min+1
holes=[0]*size
for i in arr:
    holes[i-my_min]+=1
j=0
for count in range(size):
    while holes[count]>0:
        holes[count]-=1
        arr[j]=count+my_min
        j+=1
print(arr)