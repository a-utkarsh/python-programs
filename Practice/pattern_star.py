n=5

space=" "
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
        #print("*",end=" ")
    print(" ")

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
        #print("*",end=" ")
    print(" ")
for i in range(n):
    print(("*"*i).rjust(n-1,'-')+"*"+("*"*i).ljust(n-1,"-"))


temp = 1
flag = 1
temp1 = 0
for i in range(1, 2*n):
    if(i <= n):
        print(" " * (n - i), end="")
        print("*" * temp)
        temp1 = temp
        temp += 2
    else:
        temp1 -= 2
        print(" " * flag, end="")
        print("*" * temp1)
        flag += 1
'''
flag=1
count=1
temp=1
for i in range(1,2*n):
    if(i<=n):
        print(" "*(n-i),end=" ")
        print("*"*count)
        temp=count
        count+=2
    else:
        temp-=2
#for i in range(0,n):
        print(" "*flag,end=" ")
        print("*"*temp)
        count-=2
        flag+=1
        


flag=n-2
for i in range(0,2*n-1):
    if(i<n):
        print(("*"*i).rjust(n-1)+"*"+("*"*i).ljust(n-1))
    else:
        print(("*"*flag).rjust(n-1)+"*"+(("*"*flag).ljust(n-1)))
        flag-=1

'''

n=6

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

for i in range(1,n+1):
    print(("*"*i).rjust(n))


for i in range(1,n+1):
    if(i<=n):
        print(" " * (n - i), end="")
        print("*" * i)