def flatlandSpaceStations(n, c):
    import math
    result = []
    x = []
    for i in c:
        temp = []
        for j in range(n):
            temp.append(abs(i - j))
        x.append(temp)
    for i in range(n):
        min_ = math.inf
        for j in range(len(x)):
            if (x[j][i] < min_):
                min_ = x[j][i]
        result.append(min_)
    return max(result)




nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))
print(flatlandSpaceStations(n,c))