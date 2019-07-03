Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}

Students = list(Dict.keys())
print(list(Dict.values()))
print(Students)
print(type(Students))
print(Students)
Students.sort()
print(Students)
print(str(Dict['Tim']))
for i in Students:
      print(":".join((i,str(Dict[i]))))
