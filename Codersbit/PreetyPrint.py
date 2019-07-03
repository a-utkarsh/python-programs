n=4
c=n
temp = [[0]*(2*n-1)]*(n)
k = 1
row_update = [0]*(2*n-1)
final=[]
#print(row_update)

for i in range(n):
    row = []
    for j in range(2*n-1):
        if(i == 0):
            row.append(c)

        elif(j >= (n - c) and j <= (2 * n - 1 - k)):
            row_update[j] = c
    temp[i] = row[:] if row_update[0] == 0 else row_update[:]
    row_update = row if row_update[0] == 0 else row_update
    c -= 1
    k += 1
    z=row_update[:]
    final.append(z)

    #final.append(row_update)
for i in range(len(temp)-2, -1, -1):
     final.append(final[i])
print(final)