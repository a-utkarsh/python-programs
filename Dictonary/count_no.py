arr=[1,1,3,4,2,2,3,4,1,2]
dic={}
for i in arr:
    dic[i]=dic.get(i,arr.count(i))
print(list(dic.keys()))