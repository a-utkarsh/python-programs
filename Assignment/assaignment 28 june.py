#greatest two number
x=int(input("enter the value of x :"))
y=int(input("enter the value of y :"))
if x>y:
    print(x,"is the greatest of the two .")
else:
    print(y,"is the greatest of the two.")

#greatest between three numbers
x=int(input("enter the value of x :"))
y=int(input("enter the value of y :"))
z=int(input("enter the value of z :"))
if (x>y) and (x>z):
    print(x,"is the largest no of all.")
elif y>z:
    print(y,"is the largest no of all.")
else:
    print(z,"is the largest no of all.")

#check whether the number is negative,positive or zero
num=int(input("enter any number :"))
if num>0:
    print(num,"is a positive number.")
elif num==0:
    print("number is zero")
else:
    print(num,"is a negative number :")

#check whether the number is divisible by 5 &  11 or not

num = int(input("Enter any number:"))

if(num %5 ==0) and (num% 11 == 0):
    print(num,"is divisible by 5 and 11.")
else:
    print(num,"is not divisible by 5 and 11.")

#check whether the number is even or odd
num=int(input("enter a number:"))
if (num % 2)==0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))

#leap year
year=int(input("enter a year"))
if(year % 4) ==0:
    if(year % 100) == 0:
        if(year % 400) ==0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

#Write a program to check whether a character is Alphabet or Digit or Special Character
ch=input("Enter the character : ")
if(ch.isalpha()):
    print("The character is Alphabet")
elif(ch.isdigit()):
    print("The Character is Digit")
else:
    print("The Character is a special character")


#Write a program to check whether a Alphabet is vowel or consonant
list=['a','e','i','o','u']
ch=input("Enter the character : ")
if(ch in list):
    print("The alphabet is vowel")
else:
    print("The alphabet is consonant")


#Write a program to check whether a character is Alphabet or not
ch=input("Enter the character : ")
if(ch.isalpha()):
    print("The character is Alphabet")
else:
    print("The character is not Alphabet")
