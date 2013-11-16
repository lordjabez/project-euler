with open('names.txt') as f:
    namestr = f.read()

namestr = namestr[1:-1]

names = namestr.split('","')
names.sort()

namescores = ((n+1) * sum(ord(c)-64 for c in name) for n, name in enumerate(names))
   

print(sum(namescores))
