from itertools import islice, count
A = int(input("A : "))
B = int(input("B : "))
C = int(input("C : "))
D = int(input("D : "))
list1 = []
i=1
while ((i % A == 0) or (i % B == 0) or (i % C == 0)):

    if (i==D):
        break
    list1.append(i)
    i+=1
print(len(list1))



