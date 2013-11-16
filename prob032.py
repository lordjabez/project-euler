import itertools

perms = (''.join(p) for p in itertools.permutations('123456789'))
factors = ((int(p[:2]), int(p[2:5]), int(p[:1]), int(p[1:5]), int(p[5:])) for p in perms)
solutions = (e for a, b, c, d, e in factors if a * b == e or c * d == e)
solutionset = set(solutions)
print solutionset
print sum(solutionset)
