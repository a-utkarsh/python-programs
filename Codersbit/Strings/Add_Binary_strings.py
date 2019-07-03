A="100"
B="011"
if len(A)>len(B):
    B="0"*(len(A)-len(B))+B
else:
    A = "0" * (len(B) - len(A)) + A
result=""
carry=0
for i in range(len(A)-1,-1,-1):
    #print(i,end="")
    r=carry

    r += 1 if A[i] == '1' else 0
    r += 1 if B[i] == '1' else 0
    result = ('1' if r % 2 == 1 else '0') + result
    carry = 0 if r < 2 else 1  # Compute the carry.

if carry != 0: result = '1' + result
print(result)


#another method
A=int(A,2)
B=int(B,2)

C=bin(A+B)
print(C[2:])
