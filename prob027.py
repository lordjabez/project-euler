def primegenerator(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

primes = list(primegenerator(10000000))
primeset = set(primes)

longestab = 0, 2
longestvalue = 2

for b in primes:
    if b >= 1000:
        break;
    for a in range(-999, 1000):
    #for a in range(1, 2):
        for n in range(1, 1000):
            x = n * n + a * n + b
            if x not in primeset:
                break
        if n > longestvalue:
            longestab = a, b
            longestvalue = n
            print(longestab)
            print(longestvalue)            
