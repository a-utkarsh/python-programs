from operator import itemgetter
#list1=[['Ayush', '640', '100'], ['Prateek', '670', '80'], ['Suraj', '670', '70'], ['Sameer', '620', '50'], ['Sahil', '630', '20'], ['Sumit', '640', '90']]

list1=[['Ayush', '640', '100'], ['Prateek', '670', '80'], ['Suraj', '670', '70'], ['Sameer', '670', '50'], ['Sahil', '630', '20'], ['Sumit', '640', '90']]
list2 = sorted(list1, key=itemgetter(1), reverse=True)
print(list2)
'''list3 = sorted(list2, key=itemgetter(2), reverse=True)
print(list3)'''
def reverse(a,b):
    temp=0
    temp=a
    a=b
    b=temp
    print(a,b)
    return a,b
for i in range(len(list2)-1):
    for j in range(len(list2)-i-1):
        if list2[i][1] == list2[i + 1][1]:
            if (list2[i][2] > list2[i + 1][2]):
                list2[i],list2[i + 1]= reverse(list2[i],list2[i + 1])
        else:
           list2[i], list2[i + 1] = reverse(list2[i], list2[i + 1])


print(list2)
''' list2[i + 1], list2[i] = list2[i], list2[i + 1]
        elif list2[i][2] == list2[i + 1][2]:
            if (list2[i][0] < list2[i + 1][0]):
                list2[i + 1], list2[i] = list2[i], list2[i + 1]
#    print(list2)'''


