def LCP(arr):
    #Function to find shortest common between two strings
    def LCSutil(str1,str2):
        i=0
        j=0
        res=""
        while i<len(str1) and j<len(str2):
            if str1[i]!=str2[i]:
                break
            res+=str1[i]
            i+=1
            j+=1
        return res

    arr.sort()
    return LCSutil(arr[0],arr[len(arr)-1])
arr=["appl","apple","applee"]
print(LCP(arr))