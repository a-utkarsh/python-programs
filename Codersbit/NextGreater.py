'''
A=[34, 35, 27, 42, 5, 28, 39, 20, 40]
result=[]

for i in range(len(A)-1):
    j=i+1
    while(j<len(A)):
        if(A[j]>A[i]):
            result.append(A[j])
            break
        j+=1
    else:
        result.append(-1)

result.append(-1)
print(result)

def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def pushStack(stack,item):
    stack.push(item)
def pop(stack):
    if isEmpty(stack):
        print("Underflow")
    else:
        return stack.pop()
def printNGE(arr):
    s=createStack()
    element=0
    next=0
    pushStack(s,arr[0])
    temp={}
    for i in
'''


# Python program to print next greater element using stack

# Stack Functions to be used by printNGE()
def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()


'''prints element and NGE pair for all elements of 
arr[] '''


def printNGE(arr):
    s = createStack()


    # push the first element to stack
    push(s, arr[0])
    temp = {}

    # iterate for rest of the elements
    for i in range(1, len(arr), 1):
        next = arr[i]

        if isEmpty(s) == False:

            # if stack is not empty, then pop an element from stack
            element = pop(s)

            '''If the popped element is smaller than next, then 
                a) print the pair 
                b) keep popping while elements are smaller and 
                stack is not empty '''
            while element < next:
                temp[element] = next
                if isEmpty(s) == True:
                    break
                element = pop(s)

            '''If element is greater than next, then push 
            the element back '''
            if element > next:
                push(s, element)

        '''push next to stack so that we can find 
        next greater for it '''
        push(s, next)

    '''After iterating over the loop, the remaining 
    elements in stack do not have the next greater 
    element, so print -1 for them '''

    while isEmpty(s) == False:
        element = pop(s)
        next = -1
        temp[element] = next

    for i in range(len(arr)):
        print(arr[i], "==>", temp[arr[i]])


# Driver program to test above functions
arr = [4, 5, 2, 25]
printNGE(arr)

# This code is contributed by Subodh Sawrav
