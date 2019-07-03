def pallindrome(s):
    def ispallindrome(s):
        a="".join(reversed(s))
        if a==s:
            return True
        else:
            return False

    cnt=0
    flag=0
    while len(s)>0:
        if ispallindrome(s):
            flag=1
            break
        else:
            cnt+=1
            s=s[:-1]
    if flag==1:
        return cnt
print(pallindrome("aaaaaa"))

