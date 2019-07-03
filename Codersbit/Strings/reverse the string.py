s = " the sky is blue "
x=s.split()
#x.reverse()
print(x)
res=""
for i in range(len(x)-1,-1,-1):
    res=res+" " +x[i]
print(res.strip())
print(res)