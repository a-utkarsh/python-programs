import re
s = '<html><head><title>Title</title>'
print(len(s))
print (re.match('<.*>', s).span())
print ("Greedy ", re.match('<.*>', s).group())
print("Non Greedy ", re.match('<.*?>', s).group())