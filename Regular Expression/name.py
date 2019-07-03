import re

string = 'Utkarsh is 22 years old, Hunnain is 20 years old' \
         'Monikanchan is 25 years old and his grand father Dipanjal  is 102 years old'

name = re.findall(r'[A-Z][a-z]*',string )
print(name)
age  = re.findall(r'\d{1,3}', string)

print(age)
x= 0
agedict = {}
for eachname in name:
    agedict[eachname] = age[x]
    x+=1
print(agedict)