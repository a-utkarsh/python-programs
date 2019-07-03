import re
st= "utkarsh anand lol"
first = st.capitalize()


for i  in first[:].split():
    first = first.replace(i, i.capitalize())
print(first)






#second = (re.findall(r'\s[a-z]?', first))
#print(second)

#for i in range(len(second)):

    #third =  second[i].upper()



    #final = (re.sub(r'\s[a-z]?',third , first))

#print(final)


