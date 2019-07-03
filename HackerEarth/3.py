n=int(input())
number= list(i for i in input().split())
total=list(set(number))
cnt=[]
for i in total:
    cnt.append(number.count(i))
print(len(number)-max(cnt))








