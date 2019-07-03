import string
char = string.ascii_lowercase
n  = int(input('num'))
List= []
for i in range(n):
    st  = '-'.join(char[i:n])
    List.append((st[::-1] + st[1:]).center(4 * n - 3, "-"))

print('\n'.join(List[:0:-1] + List))