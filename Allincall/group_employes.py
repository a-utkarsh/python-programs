# Binomial Sum
def select(n):
    return (1 << n)

n = int(input())
a = list(map(int,input().split()))

#-- Counting Ids
#emp = {}
l=set(a)
emp=[]
for i in l:
    emp.append(a.count(i))


# Selection
result = 0
for i in emp:
    result += (select(i) -(i+1))
print(int(result)%1000000007)