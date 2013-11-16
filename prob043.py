import itertools

perms = (''.join(p) for p in itertools.permutations('0123456789'))

div17 = (p for p in perms if int(p[7:10]) % 17 == 0)
div13 = (p for p in div17 if int(p[6:9]) % 13 == 0)
div11 = (p for p in div13 if int(p[5:8]) % 11 == 0)
div7 = (p for p in div11 if int(p[4:7]) % 7 == 0)
div5 = (p for p in div7 if int(p[3:6]) % 5 == 0)
div3 = (p for p in div5 if int(p[2:5]) % 3 == 0)
div2 = (p for p in div3 if int(p[1:4]) % 2 == 0)

print(sum(int(p) for p in div2))
