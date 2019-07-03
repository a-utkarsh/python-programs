#Find out the maximum sub-array of non negative numbers from an array.



def maxset(A):
    i = 0
    maxi = -1
    #index = 0
    a = []

    while i < len(A):
        while i < len(A) and A[i] < 0:
            i += 1
        l = []

        #index = i
        while i < len(A) and A[i] >= 0:
            l.append(A[i])
            i += 1
        #print(l)
        if (sum(l) > maxi):
            a = l
            maxi = sum(l)

    return a


A= [1, 2, 5, -7, 2, 3]
print(maxset(A))