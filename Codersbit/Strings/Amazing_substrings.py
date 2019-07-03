#find total sub strings starting with vowel
s="ABEC"
flag=0
result=[]
print(s[2:3])

i=0
j=0
amz=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(len(s)):
    str1 = ""
    for j in range(len(s)):


        if s[i] in amz:
            str1 = s[i:j+1]
            result.append(str1)
while ("" in result):
        result.remove("")

print(len(result))
#Efficient approach
res=0
amz=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(len(s)):
    if s[i] in amz:
        res+=len(s)-i
print(res)