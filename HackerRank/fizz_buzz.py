def fizzbuzz(n):
    list1= []
    for i in range(1, n+1):
        if(i%3==0 and i%5==0):
            list1.append("FizzBuzz")
        elif(i%5==0):
            list1.append("Buzz")
        elif(i%3==0):
            list1.append("Fizz")
        else:
            list1.append(i)
    print(list1)


fizzbuzz(15)

