var1 = "TThis is a python programming"
var2= "This is is python"
var3= "123"
var4 ='-'
var5 = 'abc'

print("Title:", var1.title())
print("Count of 'is':", var2.count('is'))

print("Count of 'is' with range:", var2.count('is', 0,5))
print("String ends with 'python'",var2.endswith('python'))
print("String starts with 'this':", var2.startswith('this'))
print("is 'python' there in var1:", var2.find('python'))
print("is 'python' there in var1:", var2.find('programming'))
print(var1.lstrip('T'))
print(var1.find('z'))
print(var1.strip('o'))
print(var1.rstrip('g'))
print(var1.index('h'))
#print(var1.index('z'))
print(var4.join(var5))
print(len(var1))