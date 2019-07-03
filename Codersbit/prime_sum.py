'''
def primesum(A):
    arr = []
    notprime=[]
    for i in range(2,A):
        if i not in notprime:
            arr.append(i)

            for j in range(i*i,A+1,i):
                notprime.append(j)


    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == A:
            return arr[l], arr[r]

        elif arr[l] + arr[l] == A:
            return arr[l], arr[l]

        elif arr[r] + arr[r] == A:
            return arr[r], arr[r]

        elif (arr[l] + arr[r] < A):
            l += 1
        else:
            r -= 1


print(primesum(10))
'''


def primesum(n):
    import math
    is_prime = [True] * (n + 1)

    prime=[]
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(math.sqrt(n)) + 1):

        if is_prime[i]:

            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    for i in range(len(is_prime)):
        if is_prime[i]==True:
            prime.append(i)
    print(prime)
    for i in range(2, n):
        if is_prime[i] and is_prime[n - i]:
            return [i, n - i]

    return []
print(primesum(10))