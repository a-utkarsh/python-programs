#Most efficient way to generate prime numbers
def sieve_of_eratosthenes(n):
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
    return prime
num=int(input("Enter a number: "))
print(sieve_of_eratosthenes(num))