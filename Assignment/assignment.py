var1 = "Welcome to Guwahati"
var2 = "Enjoy the city"
var3 = "goodness"
var4 = "drinkH2O"
var5 = "123"
var6 = {'x':4,'y':-5}
var7 = '\nNew Line is printable'
var8 = 'Space and Empty strings are printable'
var9 = '    \t      \n'
var10='Python Is Good.'
dict = {"a": "123", "b": "456", "c":"789"}
var11= "abc"
var12="WELCOME TO GUWAHATI"
var13="cat"
width=5
var14="cold,cold heart"



print(var4.isdigit())       #prints true only when all elements are in numbers, no spacebar can be used
print(var1.join(var5))      #joins variable by variable
#the var1 uses full sentence at once but var5 uses position by position
#the last position is var5 with no further var1
print(var3.split('d'))         #seperates each word by single inverted commas
print("The capitalize string is ", var3.capitalize())   #capitalize the first letter of var1
print(var2.count("y"))                                  #counts the number of letter 'r' present is var2
print(var2.count("y",2,14))                              #counts from location 2 till 6
print(var2.endswith("city"))                            #checks if the word 'python' is ending at the last
print(var1.startswith("Welcome"))                            #checks if it starts with "this"
print(var1.find("the"))                                  #checks the location of python
print(var2.find("city"))                                #if not present then shows "-1"
print(var1.index("to"))                                 #"This" is present in location 0
print(var4.isalnum())                                   #words ith no space shows true meaning one word
print(var3.isalpha())                                   #words with no numbers and no space shows true, else vise versa
print(var5.isdigit())                                   # if number/s present then true else false. No alphabets
print(var3.islower())                                   #all the letters should be in small letters
print(var3.isnumeric())                                 #same as digit
print(len(var1))                                        #total length of var1. starts from 1(not 0)
print(var1.__sizeof__())
print("uppercase",var1.upper())                         #converts all small letters into capital letters
print("lowercase",var1.lower())                         #converts all capital letters into small letters
print(var1.lstrip('W'))                                 #removes only the first letter of the sentence
print(var1.rstrip('i'))                                 #removes only the last letter of the sentence
print(var1.casefold())                                  #converts all capital letters to small letters
print(var1.center(21))                                  #adds the width number or add if u want to expand the distance
print(var1.encode())                                    #starts with 'b' and puts 'var1'
print(var1.expandtabs(6))                               #\t (tab) is used in var to expand
print('{x}{y}'.format_map(var6))                        #used when there is var6 type
print("Hello {}, your balance is {}.".format("Adam", 230.2))#format is used in this way directly
print(var5.isdecimal())                                 #if all the characters in the string are decimal characters
                                                        #true ELSE False
print(var4.isidentifier())                              #true if no spacebar is used ELSE False
print(var7.isprintable())
print(var8.isprintable())
print(var9.isspace())
print(var10.istitle())
print(var11.maketrans(dict))
print(var12.isupper())                                  #TRUE IF ALL ARE IN CAPITAL LETTERS
print(var1.rpartition('to'))                            #rpartition and partition are same, they both divides
print(var1.partition('to'))
print(var13.ljust(width))                               #use the distance for start and end
print(var13.rjust(width))
print(var1.rfind('to', 2))                              #adds the value and location to check distance
print(var2.rindex('the city'))                          #counts the unused word/s
print(var14.replace('cold', 'broken'))                  #1st use the word to be replaced then next new word
print(var1.splitlines())                                #puts the values of variable inside ['']
print(var1.swapcase())                                  #exchanges the caps to small and small to caps
print(var1.zfill(40))  #adds '0' in the begining and lets the values of var1 complete at the end upto the count of 40
