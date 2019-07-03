#Length of longest common subsequence using Recursion
def len_comm_subse(X,Y,i,j):
    count = 0
    if i == 0 or j == 0:
        return 0
    elif(X[i-1]==Y[j-1]):
        count=1+len_comm_subse(X,Y,i-1,j-1)
    else:
        count= max(len_comm_subse(X, Y, i-1, j), len_comm_subse(X,Y, i,j -1))
    return count

X = "ABCDGH"
Y = "AEDFHR"
print(len_comm_subse(X,Y,len(X),len(Y)))

#Dynnamic programming approach
def lenCommonSubseq(str1,str2):
    table=[[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i==0 or j==0:
                table[i][j]=0
            elif(str1[i-1]==str2[j-1]):
                table[i][j]=1+table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    return table[len(str1)-1][len(str2)-1]+1
print(lenCommonSubseq(X,Y))

#Other DP approach RBR
def lcs(str1,str2):
    m=len(str1)
    n=len(str2)
    table=[[0 for i in range(n)] for j in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if i==0 or j==0:
                table[i][j]=0
            elif(str1[i]==str2[j]):
                table[i][j]=1+table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    return table[m-1][n-1]+1
print(lcs(X,Y))
