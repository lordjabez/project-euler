# ALTERNATIVELY USE PYTHON FRACTIONS MODULE

import decimal
import itertools

dec = decimal.Decimal
decimal.getcontext().prec = 4

A = range(1, 10)
B = range(1, 10) 
C = range(1, 10)
D = range(1, 10)

digits = [(dec(a), dec(b), dec(c)) for a in A for b in B for c in C if a < b]

fracs0 = ((a / b, (a*10+c), (b*10+c)) for a, b, c in digits)
fracs1 = ((a / b, (a*10+c), (c*10+b)) for a, b, c in digits)
fracs2 = ((a / b, (c*10+a), (b*10+c)) for a, b, c in digits)
fracs3 = ((a / b, (c*10+a), (c*10+b)) for a, b, c in digits)

fracs = itertools.chain(fracs0, fracs1, fracs2, fracs3)

solutions = ((int(m), int(n)) for f, m, n in fracs if f == m / n)

print(set(solutions))
