
fname = input("Enter file name: ")

num_words = 0
total = 0

file = open(fname, 'r')
word= input("word")
for line in file:

    words = line.split()
    num_words += len(words)
    if word in line:
        total += 1
    
file.close()

print("Number of words:")
print(num_words)
print(total)
