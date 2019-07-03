import re
S='miseiittanapatimahenipur'

list2=list(S)
print(list2)
list1=['s','e','n','p','t','i','m','a','n','i','u','r']
for i in list2:
    if i not in list1:
        list2.remove(i)
