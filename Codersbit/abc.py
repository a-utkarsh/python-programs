import math


def printSubsequences(arr, n):
    opsize = math.pow(2, n)
    A = []
    C = []
    for counter in range(1, (int)(opsize)):
        B = []
        for j in range(0, n):

            if (counter & (1 << j)):
                B.append(arr[j])

        A.append(B)
    for i in A:
        if i.count(i[0]) == len(i):
            C.append(i)
    return C

def solve(A):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return set(factors)
    B = []
    C = []

    for i in A:
        B.append(math.factorial(i))
    for i in B:
        C.append(prime_factors(i))
    result = printSubsequences(C, len(C))
    return len(result)
arr=[2,3,4,5,6]
print(solve(arr))
