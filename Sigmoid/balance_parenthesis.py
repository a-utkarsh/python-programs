def checkParenthesis(str1):
    stack=[]
    open_p=['(','{','[']
    close_p=[')','}',']']
    for i in str1:
        if i in open_p:
            stack.append(i)
        elif i in close_p:
            pos=close_p.index(i)
            if(len(stack)>0 and open_p[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if (len(stack)==0):
        return "Balanced"
string = "{[]{()}}"
print(checkParenthesis(string))