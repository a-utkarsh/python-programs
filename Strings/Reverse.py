string = input("Enter a string")

'''If start is omitted it defaults to 0 and if stop is omitted it
defaults to the length of string.
-1 is telling python to start counting 1 from the stop until it reaches start'''
print(string[::-1])

print("".join(reversed(string)))

a=5
b=7
print(a,b)
b=4
print(a,b)
a,b=b,a
print(a,b)
