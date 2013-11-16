maxvalue = 1000000

primes = set(range(maxvalue))
primes.remove(0)
primes.remove(1)
for i in range(maxvalue):
    if i in primes:
        for j in range(i*i, maxvalue, i):
            primes.discard(j)

canthave = set(('2', '4', '5', '6', '8'))

for p in list(primes):
    if canthave & set(str(p)):
        primes.discard(p)

solutions = set([2, 5])

for p in primes:
    strp = str(p)
    rotations = set(int(strp[int(i):] + strp[:int(i)]) for i in range(len(strp)))
    if rotations.issubset(primes):
        solutions.add(p)

print(solutions)
print(len(solutions))