def hotel(arr,dep,k):
    aux=[]
    for i in range(len(arr)):
        aux.append((arr[i],1))
        aux.append((dep[i],0))

    aux.sort()
    count=0
    for i in range(len(aux)):
        if aux[i][1]==1:
            count+=1
            if count > k:
                return False
        else:
            count-=1

    return True
arr=[ 1, 2, 3, 4 ]
dep=[ 10, 2, 6, 14 ]
k=4
print(hotel(arr,dep,k))