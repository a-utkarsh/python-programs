#ASSIGMENT ANSWERS-2
print('1. Natural numbers from 1 to n')
print('2. All Odd Numbers Between 1 And 100')
print('3. Sum of all even Numbers')
print('4. Number of Digits in a Number')
print('5. ')
print('6. Reverse of a Number')
print('7. Factorial of a number')
print('8. All prime numbers Between 1 to n')
print('9. Fibonacci series up to n terms')
print('10. ')
choice=int(input('Enter Your Choice: '))


if choice == 1:

    #Program - Natural numbers from 1 to n

    n = int(input("Enter any number "))
    i = 1
    while i <= n:
        print(i,end=', ')
        i+=1



elif choice == 2:

    #Program - All Odd Numbers Between 1 And 100
    print(end='All odd numbers between 1 & 100 are : ')

    for i in range(101):
        if(i%2):
            print(i,end=', ')



elif choice==3:

    #Program - Sum of all even Numbers

    n = int(input("Enter any number "))
    i,sum=0,0
    while i <= n:
        if(i%2==0):
            sum+=i
        i+=1
    else:
        print('The sum is: ',sum)



elif choice==4:
    #Program - Number of Digits in a Number
    n = int(input("Enter any number "))
    count = 0

    while n!=0:
        n//=10
        count+=1

    else:
        print('Total Number of Digits: ',count)



elif choice==6:

    #Program - Reverse of a Number

    num=int(input('Any Number: '))
    temp,rev=0,0
    while num:
        temp=num%10
        rev += temp
        num //= 10
        if num:
            rev*=10

    else:
        print('Reverse is: ',rev)



elif choice==7:

    # Program - Factorial of a number.

    num = int(input('Enter a Number: '))
    factorial = 1

    if num < 0:
        print("Factorial does not exist.")

    elif num == 0:
        print("The factorial of 0 is 1")

    else:
        for i in range(1,num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)



elif choice==8:

    # Program - All prime numbers Between 1 to n

    n = int(input("Enter range: "))

    print("Prime numbers between 1 and", n, "are: ")

    for num in range(1,n + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num,end=', ')


elif choice==9:

    # Program - Fibonacci series up to n terms

    term = int(input("How many terms? "))

    n1 = 0
    n2 = 1
    count = 0

    if term <= 0:
        print("Please enter a positive integer")
    elif term == 1:
        print("Fibonacci sequence upto", term, ":")
        print(n1)
    else:
        print("Fibonacci sequence upto", term, ":")
        while count < term:
            print(n1, end=' , ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1



else:
    print('Wrong Choice!!!')
