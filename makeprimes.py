import itertools

maxvalue = 10000000

primes = set(range(maxvalue))
primes.remove(0)
primes.remove(1)
for i in range(maxvalue):
    if i in primes:
        for j in range(i*i, maxvalue, i):
            primes.discard(j)
            
primelist = list(primes)
primelist.sort()

for prime in primelist:
    print(prime)


