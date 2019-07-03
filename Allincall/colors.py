def solve( A):
    color3 = 24
    color2 = 12
    temp = 0

    for i in range(2, A + 1):


        color2 = (5 * temp + 7 * color2) % 1000000007

    num = ( color2) % 1000000007

    return num
print(solve(2))