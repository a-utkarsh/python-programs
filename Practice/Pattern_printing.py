n = 5


num=1
for i in range(n):
    for j in range(i+1):
        print(num,end="")
        if(j < i):
            print("*", end = "")
        num=num+1
    print()

temp = num - n

diff = n-1
#print(temp)
for i in range(n):
    num = temp
    for j in range(n-(i)):
        print(num, end="")
        if(j < n-i-1):
            print("*", end = "")
        num=num+1
    temp -= diff
    diff -= 1
    print()



















'''
temp = []
count = 1
for i in range(n):
    a = []
    for j in range(n-i):
        a.append(count)
        count += 1
    temp.append(a)
for i in range(1, n+1):
    a = []
    for j in range(i):
         a.append(count)
         count += 1
    temp.append(a)
x = []
y = []
for i in range(int(len(temp)/2)):
    y = temp[i]
    y.extend(temp[len(temp)-i-1])
    x.append(y)
    #print(x)

num = 0
for i, q in enumerate(x):
    for t in range(num):
        print("-", end="")
    for j, p in enumerate(q):
        print(p, end = "")
        if(j < len(q)-1):
            print("*", end = "")
    num += 2
    print()
'''