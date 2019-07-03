s="923857614"
dic={}
t="423692"
for i in range(9):
    dic[s[i]]=dic.get(s[i],i)
print(dic)
key={0:[1,3,4],1:[0,2,3,4,5],2:[4,1,5],3:[0,1,4,6,7],4:[0,1,2,3,5,6,7,8],5:[1,2,4,7,8],6:[3,4,7],7:[3,4,5,6,8],8:[7,4,5]}
count=0
for i in range(1,len(t)):
    if dic[str(t[i])] in key[dic[str(t[i-1])]]:

        count+=1
    elif(dic[str(t[i])]-dic[str(t[i-1])]==0):
        continue
    else:
        count+=2
print(count)
