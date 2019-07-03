#Remove vowels from a string
def remove_vowels(a):
    x=""
    list=['a','e','i','o','u','A','E','I','O','U']
    for i in a:
        if i not in list:
            x=x+i
    return x

a="AbacdEfghIjklmnOpqrstUvwxyz"
print(remove_vowels(a))

