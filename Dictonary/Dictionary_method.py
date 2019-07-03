Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Name: %s" % list(Dict.items()))


#print(list(Dict.items()))
#print(len(Dict))
#print(str(Dict))
print(Dict.items())

print(list(Dict.values()))

print(Dict.keys())

#print(Dict.__str__())
#Dict.__delitem__('Tim')
print(Dict)
seq = ('name', 'age', 'gender')
#print(type(seq))

dict1 = {}
print(dict1.fromkeys(seq,10))

#print(Dict.setdefault('Tim'))
#print(Dict[('Tim')])