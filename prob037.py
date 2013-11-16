import math

maxdigits = 10

def isprime(n):
    if n in (0, 1):
        return False
    if n == 2:
        return True
    divs = range(2, int(math.sqrt(n))+2)
    return all(n % d for d in divs)

digits = '123579'

leftprimes = [['']]
rightprimes = [['']]

for i in range(1, maxdigits):
    leftprimegen = (d + p for d in digits for p in leftprimes[i-1])
    leftprimes.append([n for n in leftprimegen if isprime(int(n))])

leftprimes = [int(p) for n in leftprimes for p in n if len(p) > 1]

for i in range(1, maxdigits):
    rightprimegen = (p + d for d in digits for p in rightprimes[i-1])
    rightprimes.append([n for n in rightprimegen if isprime(int(n))])

rightprimes = [int(p) for n in rightprimes for p in n if len(p) > 1]

leftandright = set(leftprimes) & set(rightprimes)

print(leftandright)
print(len(leftandright))
print(sum(leftandright))