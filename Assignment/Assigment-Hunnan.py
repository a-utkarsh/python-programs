#ALL ASSIGNMENT ANSWERS
print('1.Maximum of 2 numbers')
print('2.Maximum of three numbers')
print('3.Positive,Negative or Zero')
print('4.Divisible By 5 & 11')
print('5.Odd or Even')
print('6.Leap year')
print('7.Alphabet or not')
print('8.Vowel or Consonant')
print('9.Alphabet, Digit or Special Character')
choice=int(input('\nEnter your choice: '))
print('\n')



if choice == 1:
    # Program - Find Largest of Two Numbers
    print("Enter any two numbers: ")
    number1 = int(input())
    number2 = int(input())
    count = 0
    if number1 > number2:
    	largest = number1
    	count = 1
    elif number1 < number2:
    	largest = number2
    	count = 1
    else:
        print("\nBoth the numbers are equal to each other.")
    if count == 1:
        print("\nLargest of the given two numbers is", largest)



elif choice==2:
    #Program - Find Largest of Three Numbers
    print("Enter any three numbers: ")
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    largest = number1
    count = 1
    if largest < number2:
        if number2 > number3:
            largest = number2
        else:
            largest = number3
    elif largest < number3:
         if number3 > number2:
            largest = number3
         else:
            largest = number2
    else:
         largest = number1

    if number1 == number2:
         if number1 == number3:
            count = 0
    if count == 0:
         print("\nAll numbers are equal to each other.")
    else:
         print("\nLargest of the given three numbers is", largest)



elif choice==3:
    #Program - Positive,Negative or Zero
    num = float(input("Enter any number : "))
    if num >= 0:
        if (num == 0):
            print("Given number is Zero")
        else:
            print("Given number is Positive number")
    else:
        print("Given number is Negative number")



elif choice==4:
    #Program - Divisible by 5 & 11
    num = int(input("Enter any number : "))
    if (num%5)== 0:
        if (num%11==0):
            print("Given number is divisble by both 5 and 11")
        else:
            print("Given number is not divisible by 11")
    else:
        print("Given number is Not divisible by 5")



elif choice==5:
    #Program - Even Odd
    a = int(input("Please Enter a Number : "))
    if (a % 2 == 0):
        print("This Number is Even")
    else:
        print("This Number is Odd")



elif choice==6:
    # Program - Leap year or not

    year =int(input('Enter a Year :'))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))



elif choice==7:
    #Program - Alphabet or Not

    ch = input("Enter any character: ")
    if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        print(ch, "is an alphabet.")
    else:
        print(ch, "is not an alphabet.")



elif choice==8:
    #Program - Vowel or Consonant
    l = input("Input a letter of the alphabet: ")

    if l in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
        print("%s is a vowel." % l)
    else:
        print("%s is a consonant." % l)



elif choice==9:
    #Program - Alphabet, Digit or Special Character

    char=input('Enter a Character: ')

    if ((int(ord(char)) >= 65 and int(ord(char)) <= 90)):
        print(char,"is Alphabet ")

    elif (int(ord(char)) >= 97 and int(ord(char)) <= 122):
        print(char,"is Alphabet")

    elif (int(ord(char)) >= 48 and int(ord(char)) <= 57):
        print(char,"is Digit ")

    else:
        print(char,"is Special Character ")



else:
    print('Wrong Choice!!!')