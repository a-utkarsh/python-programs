A=[4,1,3,5,2,5,3,7,8,9,5,4]
dic={}
temp=[]
for i in A:
    dic[i]=A.count(i)
sort=sorted(dic.items(),key=lambda s:s[1],reverse=True)
for i in sort:
    for j in range(i[1]):
        print(i[0],end=" ")
'''
for a in A:
    dic[a] = dic.get(a, 0) + 1
    #print(dic)
    
temp = []
for a in dic.keys():
    temp.append([a, dic[a]])
temp = sorted(temp , key=lambda s:s[1], reverse=True)

for i in temp:
    for j in range(i[1]):
        print(i[0], end =" ")
'''