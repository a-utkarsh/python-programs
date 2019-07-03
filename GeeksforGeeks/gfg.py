
def gfg(s):

    cnt= s.count('gfg')
    if cnt>0:
        print(cnt)
    else:
        print(-1)
T=int(input())
string=[]
for i in range(T):
    st=input()
    string.append(st)
for j in string:
    gfg(j)