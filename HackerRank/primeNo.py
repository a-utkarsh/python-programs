N=int(input("Enter number:"))
j=2
for i in range(N+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end= ' ')

