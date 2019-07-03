string = input("Enter a number or string ")
a= ("".join(reversed(string)))

if (a==string):
    print("Number or string is palindrome")
else:
    print("not pallindrome")