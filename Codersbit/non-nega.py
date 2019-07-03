def fragment(a):
    frag = []
    temp = []

    for x in a:
        if(x > 0):

            temp.append(x)
        else:
            if(len(temp) != 0):
                frag.append(temp)
            temp = []
    if(len(temp) != 0):
        frag.append(temp)
    return frag

a = [5, 6, 7, -3, -2, 2, -2, 3]
print(fragment(a))