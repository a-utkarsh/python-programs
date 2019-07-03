def isPrime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False


        else:
            return True
    else:
        return False

def prime1to(n):
    for i in range(n+1):
        if isPrime(i):
            print(i,end="")
            if(i<n):
                print(",",end="")

num= int(input("Enter number"))
prime1to(num)