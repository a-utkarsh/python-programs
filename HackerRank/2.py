import itertools, re

words= ( [''.join(x) for x in itertools.product('aeiou', repeat=3)])
list1= []

for item in words:
    if re.match(r'[a][ie]',item) or re.match(r'[e][i]', item) or re.match(r'[i][aeou]', item) \
           or  re.match(r'[o][au]', item) or re.match(r'[u][oe]', item):
        list1.append(item)



print(len(list1))



