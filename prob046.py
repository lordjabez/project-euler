import itertools

with open('primes.txt') as f:
    primes = [int(line) for line in f]

odds = (n * 2 + 1 for n in range(1, 1000000))
oddcomposites = (n for n in odds if n not in primes)

primeset = set(primes)

squares2 = [2 * n * n for n in range(1000000)]

for n in oddcomposites:
    found = False
    for s in itertools.takewhile(lambda s: s < n, squares2):
        d = n - s
        if d in primeset:
            print(n, d, s)
            found = True
            break
    if not found:
        print('GOT IT:', n)
        break