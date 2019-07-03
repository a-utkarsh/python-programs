a = int(input())
A = map(int, input().split())
arr1 = list(A)
c = int(input())
C = map(int, input().split())
arr2 = list(C)
B = []
for i in range(1, 100 + 1):
    c = 0
    for j in range(len(arr2)):
        if arr2[j] - i in arr1:
            c += 1
    if c == a:
        B.append(i)
B.sort()
for i in B:
    print(i, end=" ")
