import itertools

with open('primes.txt') as f:
    primes = [int(line) for line in f]

primeset = set(primes)


perms = ((int(''.join(p)) for p in itertools.permutations(c)) for c in itertools.combinations_with_replacement('0123456789', 4))

primeperms = ([n for n in p if n in primeset and n > 999] for p in perms)
primeperms = (p for p in primeperms if len(p) > 2)

for perm in primeperms:
    setsofthree = itertools.combinations(perm, 3)
    seq = [s for s in setsofthree if s[2] - s[1] == s[1] - s[0] and s[1] != s[0]]
    if seq:
        print(seq)
