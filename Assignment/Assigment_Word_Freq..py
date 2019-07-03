num_words = 0

file = open('austen.txt', 'r')

str = file.read()

wordlist = str.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
    num_words += len(wordlist)


print("Pairs: \n" , list(zip(wordlist, wordfreq)))

print("Number of words: ", num_words)
print('Maximum frequency word:' , max(wordlist, key=wordlist.count))
print('Minimum frequency word:' , min(wordlist, key=wordlist.count))
