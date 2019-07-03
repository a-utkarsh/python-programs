Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(Dict)
del Dict ['Charlie']
print(Dict)

#Ex-2

# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)

# remove a particular item

print(squares.pop(4))
print(squares)

print(squares.popitem())
print(squares)

# delete a particular item



print(squares)

squares.clear()


print(squares)

# delete the dictionary itself
del squares


# Throws Error
# print(squares)