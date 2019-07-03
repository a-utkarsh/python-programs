import re
var1= "Aman is 22 years old, Utkarsh is 20 years old," \
      "and Aviral is 102 yaers old."

name=re.findall(r'[A-Z][a-z]*',var1)
print(name)
age=re.findall(r'\d{1,3}',var1)
print(age)