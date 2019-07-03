x  = int(input('x'))
y =  int(input('y'))
z= int(input('z'))
N =  int(input('n'))
list1 = []
p=0


for i in range(0,x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if (i+j+k!=N):
                list1.append([])
                #print(list1)
                list1[p]= [i , j, k]
                p+=1


print(list1)
