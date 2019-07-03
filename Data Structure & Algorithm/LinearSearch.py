'''Linear Search Implementation'''
def linearSearch(list,key):
    pos=0
    while pos<=len(list):
    #for i in range(len(list)):
        if list[pos]==key:
            print("Key found at position", pos)
            break
        else:
            pos+=1
list1= [1,2,4,5,9,3,8]
linearSearch(list1, 8)

