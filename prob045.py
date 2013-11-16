import itertools

triangulars = set(n * (n + 1) // 2 for n in range(1, 100000))
pentagonals = set(n * (3 * n - 1) // 2 for n in range(1, 100000))
hexagonals = set(n * (2 * n - 1) for n in range(1, 100000))

solutions = triangulars & pentagonals & hexagonals

print(solutions)