import functools
import operator

s = ''.join(str(n) for n in range(1000000))
c = functools.reduce(operator.mul, (int(s[10**i]) for i in range(7)))
print(c)