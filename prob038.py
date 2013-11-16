import math
import itertools

pandigitals = set(int(''.join(n)) for n in itertools.permutations('123456789'))

solutions = set()

for n in range(1, 10000):
    k = 1
    c = 0
    while c < 987654321:
        c = int(str(c) + str(k * n))
        if k > 1 and c in pandigitals:
            solutions.add(c)
        k += 1

print(solutions)
print
print(max(solutions))