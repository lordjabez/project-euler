import functools
import itertools
import operator

def primegenerator(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

primes = list(primegenerator(28124))

def getfactors(n):
    factors = {}
    for p in primes:
        if p > n:
            break
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    return factors

factors = [getfactors(n) for n in range(28124)]

def powered(factors, powers):
    return functools.reduce(operator.mul, (f**p for f, p in zip(factors, powers)), 1)
    
def getdivisors(n):
    primes = factors[n].keys()
    exponents = [range(i+1) for i in factors[n].values()]
    return (powered(primes, a) for a in itertools.product(*exponents))
    
divisors = [list(getdivisors(n)) for n in range(28124)]

abundants = []

for d, divs in enumerate(divisors):
    if sum(divs) > d * 2 and d > 0:
        abundants.append(d)

abundantset = set(abundants)

cantdoit = []

for n in range(1, 28124):
    found = False
    for a in abundants:
        if a >= n:
            break
        delta = n - a
        if delta in abundantset:
            found = True
            break
    if not found:
        cantdoit.append(n)

print(cantdoit)
print(sum(cantdoit))