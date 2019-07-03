
def vowels():
    s=input()
    qur=int(input())
    q=[]
    for i in range(qur):

        chr,st=map(str,input().split())
        q.append((chr,st))
    vowels=["a","e","i","o","u"]
    conso=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    for i in q:
        if i[0]=="v":
            for j in s:
                if j in vowels:
                    s=s.replace(j,i[1])
        else:
            for j in s:
                if j in conso:
                    s=s.replace(j,i[1])
    return s


t=int(input())
for i in range(t):
    print(vowels())