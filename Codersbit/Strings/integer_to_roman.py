def intToRoman(A):
    roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
             900: "CM", 1000: "M"}
    result = ""
    key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    val=['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    if A < 4000:
        for i in range(len(key)):
            if (A // key[i] > 0):
                result += (val[i] * (A // key[i]))
                A = A % key[i]
    return result



x=(intToRoman(3287))
print((x))

def romanToInt(A):
    result = 0
    key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    val = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    i=0
    rs=0
    if(A[len(A)-2]+A[len(A)-1] in val):
        rp=0
    else:
        rp=key[val.index(A[len(A)-1])]

    while i<len(A)-1:
  
        if (A[i] in val):
            if (A[i] + A[i + 1] in val):
                rs += key[val.index(A[i] + A[i + 1])]
                i += 2
            else:
                result += key[val.index(A[i])]
                print("res", result, i)
                i += 1


    return result+rs+rp


print(romanToInt("IXIX"))