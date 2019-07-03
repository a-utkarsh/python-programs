s1 = "zbcve"
s2 = "abxte"
for i in s1:
    if i in s2:
        s1 = s1.replace(i,"")
        s2 = s2.replace(i,"")
z = s2+s1
res = sorted(list(z))
final = "".join(res)
print(final)