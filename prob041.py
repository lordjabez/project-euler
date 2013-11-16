# obviously no pandigital numbers larger than 987654321
# can't have 8 or 9 digits because those sums are div by 3, and hence whole number is

import itertools
import math

def isprime(n):
    divs = range(2, int(math.sqrt(n))+2)
    return all(n % d for d in divs)

nums = (int(''.join(n)) for n in itertools.chain(itertools.permutations('1234'), itertools.permutations('1234567')))

primes = (n for n in nums if isprime(n))

print(max(primes))
