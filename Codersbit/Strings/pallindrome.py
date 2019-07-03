import re
A="A MA1n, a plan, a canal: Panama"

C=A.lower()
final=re.sub(r'\W',"",C)
print(final)