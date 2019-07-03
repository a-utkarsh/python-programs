'''
Let a[] = { 1, 2, 3 }

All subarrays are {}, {1}, {2}, {3}, {1, 2},
                     {1, 3}, {2, 3}, {1, 2, 3}

So sum of subarrays are 0 + 1 + 2 + 3 + 3 +
                             4 + 5 + 8 = 24

Here we can observe that in sum every elements
occurs 4 times. Or in general every element
will occur 2^(n-1) times. And we can also
observe that sum of array elements is 6. So
final result will be 6*4.
'''
def sumSubsequences(A):
    return sum(A)*(1<<len(A)-1)
A=[1,2,3]
print(sumSubsequences(A))