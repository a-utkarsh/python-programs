n = int(input('n'))
arr = map(int, input('arr').split())
list1 = list(arr)
print(list1)
x= max(list1)
while (max(list1)==x) :
    y = list1.remove(x)
print(max(list1))



