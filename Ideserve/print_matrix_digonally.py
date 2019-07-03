arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
for i in range(len(arr)):
    for j in range(len(arr[i])):

        print(arr[i][j],end=' ')
    print()
print(" Matrix diagonally")
rowCount=len(arr)
columnCount=len(arr[0])
i=0
while i<rowCount:
    row=i
    col=0
    while row>=0 and col<columnCount:
        print(arr[row][col],end=" ")
        row-=1
        col+=1
    i+=1
    print()
i=1
while i<columnCount:
    row=rowCount-1
    col=i
    while row >= 0 and col < columnCount:
        print(arr[row][col],end=" ")

        row -= 1
        col += 1
    print()
    i += 1


