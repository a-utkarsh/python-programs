s=input()
x=list(s)

if s.__contains__(".") and s.index(".")==len(s)-1:
    print(False)
else:

    if s.isdecimal()==True:
        print("True")

    #elif "e" in s and s.index("e")==0 or s.index("e")== len(s)-1:
    #    print("False")

    elif s.isalnum()==True:
        print("False")


    else:
        print(True)