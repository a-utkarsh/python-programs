


def findMedian(A):
    import statistics
    B=[]
    for i in A:
        for j in i:
            B.append(j)

    return statistics.median(B)
A=[[1, 3, 5],[2, 6, 9],[3, 6, 9]]


print(findMedian(A))