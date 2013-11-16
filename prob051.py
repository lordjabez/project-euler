import itertools

with open('primes.txt') as f:
    primes = [int(line) for line in f]

primeset = set(primes)

longest = 1

for p, prime in enumerate(primes):
    if prime >= 1000000:
        break
    total = prime
    q = p
    
    while total < 1000000:
        q += 1
        total += primes[q]
        length = q - p + 1
        if total in primeset and length > longest:
            print(prime, length, total)
            longest = length
        