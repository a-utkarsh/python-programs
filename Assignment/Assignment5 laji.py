#1) Write a program to find maximum between two numbers.
number = 32,76
print (max(number))  #the maximum number between 25 and 48 is 48


#2) Write a program to find mximun between three numbers.
number = 22,9,33
print (max(number))


#3) Write a program to check whether a number is negative, positive or zero
number = int(input("enter the numbers:"))
if number < 0:
    print("the entered number is negative")
elif number > 0:
    print("the entered number is positive")
elif number == 0:
    print("the number is zero")
else:
    print("input is not a number")


#4) Write a program to check whether a number is divisible by 5 and 11 or not.
num = int(input("Enter a number: "))    #shows for numbers divisible 5 and 11
if ((num % 5) == 0):
    print("{} is divisible by 5".format(num))
else:
    print("{} is not divisible by 5".format(num))
if ((num % 11) == 0):
        print ("{} is divisible by 11".format(num))
else:
    print("{} is not divisible by 11".format(num))

#to check if the input number is divisible by both 5 and 11
num = int(input("Enter a number: "))
if (num % 5 ==0 and num % 11 == 0):
    print("{} is divisible by 5 and 11".format(num))
else:
    print("{} is not divisible by 5 and 11".format(num))


    # checks by using range
    lower = int(input("Lower Range :"))
    upper = int(input("Upper Range :"))
    for i in range(lower, upper + 1):
        if (i % 5 == 0 and i % 11 == 0):
            print(i)


#5) Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))
if (num % 2 == 0):
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))



#6) Write a program to check whether a year is a leap year
year = int(input("Enter a year :"))
if (year % 4 == 0):                 # 4 because leap year occurs once every 4years
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))


#7) Write a program to check whether the character is alphabet or not.
char =input("Enter any character :")
if (char.isalpha()):
    print(char," is an Alphabet")
else:
    print(char," is not an Alphabet")
print(char.isalpha())

#8) Write a program to input any alphabet and check whether it is vowel or not.
String = str(input("Enter an alphabet :"))
if String in ('a','e','i','o','u'):
    print("the entered alphabet is a vowel")
else:
    print("the entered alphabet is not a vowel")


#9) Write a program to input any character and check whether it is alphabet,digit or special character.
char =input("Enter any character :")
if (char.isalpha()):
    print(char," is an Alphabet")
elif(char.isdigit()):
    print(char," is a digit")
else:
    print(char," is a special character")