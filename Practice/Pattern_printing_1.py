num=5
count=1
for i in range(num):
    for j in range(i+1):
        print(count,end="")
        if(j<i):
            print("*",end="")
        count+=1
    print()

temp=count-num

diff=num-1

for i in range(num):
    count=temp
    for j in range(num-i):
        print(count,end="")
        if(j<num-i-1):
            print("*",end="")
        count+=1
    temp-=diff
    diff-=1
    print()
