A=[4,8,5,2,4]
N=len(A)
p=0
k=4
sub_sum=0
A.append(k+1)
flag=0
for i in range(N+1):
    if(A[i]>k):
        if flag==1:
            sub_sum+=i-p
            flag=0
        p=i+1
    elif(A[i]==k):
        flag=1
print(sub_sum)
