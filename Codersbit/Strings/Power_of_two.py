def power(A):
    x = int(A)
    if (x == 0 or x == 1):
        return 0
    else:

        i = 1
        while (i < x):
            i *= 2
        if (i % x) == 0:
            return 1
        else:
            return 0


#Other method
def powercheck(n):
    if n == 1 or n==0:
        return 0
    if n & (n - 1) == 0:

        return 1
    else:
        
        return 0

x=int(input("Enter a number"))
print(power(x),powercheck(x))
