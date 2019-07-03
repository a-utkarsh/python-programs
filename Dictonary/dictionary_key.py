#Check if a given key already exists in a dictionary

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Boys.keys()):
    if key in list(Dict.keys()):
        print(True)
    else:
        print(False)
