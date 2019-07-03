def gfgSUbsequences(S):
    arr=[0]*100
    cntG=0
    cntF=0
    result=0

    for i in range(len(S)):
        if(S[i]=="G"):
            arr[i]=cntF
            result+=arr[i]
            cntG+=1
        elif(S[i]=="F"):
            arr[i] = cntG
            cntF += arr[i]
        else:
            continue
    return result
S="GFGFG"
print(gfgSUbsequences(S))