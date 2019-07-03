n = int(input())
for i in range(1,n+1):
    print(str(i).rjust(2, ' '), str(oct(i)[2:]).rjust(2, ' '),
                    str(hex(i)[2:]).rjust(2, ' '), str(bin(i)[2:]).rjust(len(str(bin(4)[2:])), ' '), end='   ' "\n")

