import itertools

pentagonallist = [n * (3 * n - 1) // 2 for n in range(1, 10000)]
pentagonalset = set(pentagonallist)


for p, q in itertools.product(pentagonallist, pentagonallist):
    if p <= q:
        continue
    if p + q in pentagonalset and p - q in pentagonalset:
        print(p, q, p - q)
