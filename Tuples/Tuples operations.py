tup1 = ('harry', 'utkarsh')
tup2 = (1,2,3)

#Creating a new tuple from existing tuple
tup3 = tup1+tup2
print(tup3)

#creating tuple by adding tuple values

tup4 = (1,2,3) + ('a','b','c')
print(tup4)
print(tup4[3:])

print(len(tup4))

#repeating a value in tuple
tup5 = ('a',)*8
print(tup5)

# check value in tuple
print(2 in tup4)

for i in tup4:
    print(i)
