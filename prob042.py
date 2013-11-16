with open('words.txt') as f:
    wordstr = f.read()

wordstr = wordstr[1:-1]

words = wordstr.split('","')
words.sort()

triangulars = set(n*(n+1)//2 for n in range(100000))

offset = ord('A') - 1

wordsums = ((word, sum(ord(c) - offset for c in word)) for word in words)
trianglewords = (word for word, wordsum in wordsums if wordsum in triangulars)

print(sum(1 for word in trianglewords))
#print(list(trianglewords))