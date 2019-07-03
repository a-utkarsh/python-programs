def painter(A,B,C):
    '''
    time=0
    if A==1:
        for i in C:
            time=time+B*i
            return time
    elif len(C)/A<A:
        time=max(C)*B
        return time
    else:
        for i in range(len(C)-1,len(C)-A-1,-1):

            time=time+C[i]*B
        return time%
    '''
    def valid(A,C,m):
            p=1
            i=0
            s=0
            while i<len(C):
                s+=C[i]
                if s>m:
                    s=C[i]
                    p+=1
                    if s>m or p>A:
                        return False
                i+=1
            return True


    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer

    low=C[0]
    high=sum(C)%10000003
    while low<high:
        mid=low+(high-low)//2
        if valid(A,C,mid):
            high=mid
        else:
            low=mid+1
    return int(((low%10000003)*B)%10000003)


print(painter(2,1,[10,20,30,40]))