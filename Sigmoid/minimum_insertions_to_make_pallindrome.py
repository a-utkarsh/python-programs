#Naive Approach to find minimum insertions
def findMinInsertions(str1,l,h):
    import math
    if l>h:
        return math.inf
    if l==h:
        return 0
    if l==h-1:
        if(str1[l]==str1[h]):
            return 0
        else:
            return 1
    if(str1[l]==str1[h]):
        return findMinInsertions(str1,l+1,h-1)
    else:
        return min(findMinInsertions(str1,l,h-1),findMinInsertions(str1,l+1,h))+1
print(findMinInsertions("abc",0,2))

#Dynamic programming approach for finding minimum insertions

def findMinimumInsertionsDP(str1,n):
    table=[[0 for i in range(n)]for j in range(n)]

    for gap in range(1,n):
        l=0
        for h in range(gap,n):
            if(str1[l]==str1[h]):
                table[l][h]=table[l+1][h-1]
            else:
                table[l][h]=min(table[l][h-1],table[l+1][h])+1
            l+=1
    return table[0][n-1]
str1 = "BANANA"
print(findMinimumInsertionsDP(str1, len(str1)))


