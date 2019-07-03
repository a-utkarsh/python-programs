A= [3, 30, 34, 5, 9]
'''
res= ""
for item in A:
    res+=str(item)
final= reversed(sorted(res))
largest= ""
for i in final:
    largest+=i
print(int(largest))
'''
from functools import cmp_to_key
A= map(str, A)


key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
res = ''.join(sorted(A, key= key, reverse=True))
# Must left trim 0, apparently
res = res.lstrip('0')
print(res)
