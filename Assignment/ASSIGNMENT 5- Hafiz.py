

                                         #maximum
'''
x=int(input('enter first number x:'))
y=int(input('enter second number y:'))
max= 'x is greater' if x>y else 'y is greater'
print(max)
'''

                                    #maximum of three
'''
x=int(input('enter first number x:'))
y=int(input('enter second number y:'))
z=int(input('enter third number z:'))

if (x>y):
    if (x>z):
        print('x is greater')
    else :
        print('y is greater')

elif (z>x):
    if(y>z):
        print('y  is grater')
    else:
        print('z is greater')
else :
    print('all are equal')

'''
                               #negetive, positive  or zero

'''x=int(input('enter a number x:'))

if (x>0):
    print('no is positive')
elif (x<0):
    print('no is negative')
else :
    print('no. is zero')
'''

                                #divisible by 5 and 11 or not

'''
x=int(input('enter a number x:'))
if (x%11==0):
    if (x%5==0):
        print('x is divisible by both 11 and 5')
    else:
        print('not divisible by both 11 and 5')

else :
    print('not divisible by 11 and 5')
'''

'''#even or odd

x=int(input('enter a number x:'))
if(x%2==0):
    print('x is even')
else:
    print('x is odd')
'''


                                     #leap year

'''
x=int(input('enter a number x:'))
if (x % 4) == 0:
   if (x % 100) == 0:
       if (x % 400) == 0:
           print("x is a leap year")
       else:
           print("x is not a leap year")
   else:
       print("x is a leap year")
else:
   print("x is not a leap year")
'''

                              #alphabet or not
'''
x=(input('enter x:'))
if (x.isalpha()):
    print('is a aphabet')
elif(x.isnumeric()):
    print('is a number')
else:
    print('neither no. nor alphabet')
'''


                              #VOWEL  OR CONSONANT

'''
x=('a','e','i','o','u','A','E','I','O','U')
input=input('enter an alphabet:')
if (x.__contains__(input)):
    print('is vowel')
else:
    print('consonant')

'''

                                #number, alphabet or special character

'''x=(input('enter x:'))
if (x.isalpha()):
    print('is a aphabet')
elif(x.isnumeric()):
    print('is a number')
else:
    print('special character')
'''