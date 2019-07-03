# code
def sumdigit(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot
def digital_root(n):
    if n < 10:
        return n
    return digital_root(sumdigit(n))

def digitalRoot(Number):
    div = []
    for i in range(1, Number + 1):
        if Number % i ==0:
            div.append(i)
    num1=[]
    result=[]
    for i in div:
       num1.append(digital_root(i))

    index = div.index(max(num1))
    if num1.count(max(num1))>1:
        result.append(max(div))
    else:
        result.append(div[index])
    result.append(max(num1))
    for j in result:
        print(j,end=" ")
T= int(input())
cases=[]
for i in range(T):
    N=int(input())
    cases.append(N)
for j in cases:
    digitalRoot(j)
    print()


