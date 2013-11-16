import math

solutions = [0]

for p in range(1, 1001):
    psq = p * p
    twop = p * 2
    solutions.append(0)
    for a in range(1, p//2):
        twoa = 2 * a
        b = (psq - twoa * p) / (twop - twoa)
        if b.is_integer():
            solutions[p] += 1

largest = 0
for p, s in enumerate(solutions):
    if s > largest:
        largest = s
        print(p, s)
