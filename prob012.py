import sys

def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

primes = list(primes_sieve2(1000000))


def triangular_generator(limit):
    n = 0
    for i in range(limit):
        n += i + 1
        yield n

triangulars = triangular_generator(100000)

def getfactorcount(n):
    factors = {}
    for p in primes:
        if p > n:
            break
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    factorcount = 1
    for v in factors.values():
        factorcount *= (v+1)
    return factorcount
    

for t in triangulars:
    f = getfactorcount(t)
    print(t, f)
    if f > 500:
        sys.exit()
