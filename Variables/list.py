list1 = [ 'abcd', 786 , 2.23, 'iiitm', 70.2 ]
list2 = [123, 'iiitm']
print(list1)
'''
print (list1[0])       # Prints first element of the list
print (list1[1:3])     # Prints elements starting from 2nd till 3rd
print (list1[2:])      # Prints elements starting from 3rd element
print (list2 * 2)  # Prints list two times
print(list1*2)
print(list1+list2)
'''
list1.append("abc")
print(list1)
list1.append('utkarsh')
print(list1)
list1.insert(2,"manipur")
print(list1)
list1.pop(2)
print(list1)
print(list1.count(786))
list1.reverse()
print(list1)
list3=[8,9,5,2,1]
list3.sort(reverse=True)
print(list3)

print("abcd" in list1)


print(list1.__contains__('abcd'))

list1.clear()
print(list1)