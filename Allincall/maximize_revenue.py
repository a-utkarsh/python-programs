n = int(input())
dic = {}
while (n):
    temp = list(map(int, input().split()))
    i = temp[1]
    while (i):
        dic[i] = dic.get(i, [])
        dic[i].append(temp[0])
        i -= 1
    n -= 1

temp = []
maximum=max(dic.keys())

for i in range(maximum, 0, -1):
    flag = dic[i]
    for j in range(len(temp)):
        flag.remove(temp[j])
    if (len(flag) > 0):
        temp.append(max(flag))

print(sum(temp))