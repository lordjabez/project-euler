import itertools

with open('primes.txt') as f:
    primes = [int(line) for line in f]

def numdistinctfactors(n):
    possiblefactors = itertools.takewhile(lambda p: p//2 <= n, primes)
    count = 0
    for p in possiblefactors:
        if n % p == 0:
            count += 1
        if count > 4:
            break
    return count

factorcount = (numdistinctfactors(n) for n in range(1000000))

length = 0
prevvalue = 0
longest = 0

for n, f in enumerate(factorcount):
    if f != prevvalue:
        length = 0
    length += 1
    prevvalue = f
    if length == f and length > longest:
        longest = length
        print(n, length, f)
