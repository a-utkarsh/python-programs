def s(A,B):
    res = []
    C=0
    if B > 26:
        C= B - 26
    print(C)

    for i in A:
        res.append(A.count(i))
    for i in range(len(A)):
        if res[i] % 2 == 0:
            if B<=26:
                res[i] = B + ord(A[i])
            else:
                res[i]=ord(A[i])-C

        res[i]=ord(A[i])-C
    for i in range(len(res)):
        res[i] = chr(res[i])
    x = "".join(map(str, res))
    return x
A= "wvmctuj"
B=28
print(s(A,B))