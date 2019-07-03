def countnndSay(n):
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"
    s = "11"
    for i in range(3, n + 1):
        s += '_'
        cnt = 1
        tmp = ""

        for j in range(1,len(s)):
            if (s[j] != s[j - 1]):
                tmp += str(cnt)

                tmp += s[j - 1]
                cnt = 1
            else:
                cnt += 1

        s = tmp

    return s
print(countnndSay(5))