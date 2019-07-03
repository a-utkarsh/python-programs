def nthUglyno(n):
    ugl=[0]*(n)
    ugl[0]=1
    i2=i3=i5=0
    next_multile_of_2=ugl[i2]*2
    next_multile_of_3=ugl[i3]*3
    next_multile_of_5=ugl[i5]*5
    for i in range(1,n):
        next_ugl_no= min(next_multile_of_2,next_multile_of_3,next_multile_of_5)
        ugl[i]=next_ugl_no
        if(next_ugl_no==next_multile_of_2):
            i2+=1
            next_multile_of_2=ugl[i2]*2
        if (next_ugl_no == next_multile_of_3):
            i3 += 1
            next_multile_of_3 = ugl[i3] * 3
        if (next_ugl_no == next_multile_of_5):
            i5+=1
            next_multile_of_5 =ugl[i5]*5

    return ugl[-1]
n=int(input())
print(nthUglyno(n))