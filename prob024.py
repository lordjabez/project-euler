import timeit

setup = """\
import math

factorial = [math.factorial(n) for n in range(11)]

def getpermutation(p, numdigits, digits):
    if p == 0:
        return digits
    numsubperms = factorial[numdigits-1]
    index = p // numsubperms
    newdigits = digits[:index] + digits[index+1:]
    return digits[index] + getpermutation(p % numsubperms, numdigits - 1, newdigits)

digits = '0123456789'
"""

t = timeit.timeit('getpermutation(999999, len(digits), digits)', setup=setup, number=200000)
print(t)