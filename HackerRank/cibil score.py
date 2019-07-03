from operator import itemgetter

def reverse(a,b):
    temp=0
    temp=a
    a=b
    b=temp
    #print(a,b)
    return a,b

def cibil(number):

    list1=[]
    for i in range(number):
        na, c, r=list(map(str, input().split()))
        list1.append([na,c,r])
    #print(list1)
    list2 = sorted(list1, key=itemgetter(1), reverse=True)

    for i in range(len(list2)-1):
        if list2[i][1]==list2[i+1][1]:
            if (list2[i][2] > list2[i + 1][2]):
                list2[i], list2[i + 1] = reverse(list2[i], list2[i + 1])

            elif list2[i][2]==list2[i+1][2]:
                if (list2[i][0]<list2[i+1][0]):
                    list2[i], list2[i + 1] = reverse(list2[i], list2[i + 1])

            else:
                list2[i], list2[i + 1] = reverse(list2[i], list2[i + 1])

    #print(list2)
    pos=int(input())
    list3=(list2[pos-1])
    x, y =list3[0],list3[1]
    return x, y
T=int(input())
list4=[]
for i in range(T):
    num=int(input())
    list4.append(cibil(num))
for item in list4:
    print(item[0],item[1])
