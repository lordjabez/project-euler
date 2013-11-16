import math

divisorsum = [0]

for n in range(1, 25321):
    divs = []
    for k in range(1, (n // 2) + 2):
        if n % k == 0 and k < n:
            divs.append(k)
    #print(n, divs, sum(divs))
    divisorsum.append(sum(divs))

print(max(divisorsum))

amicables = []

for a in range(1, 10000):
    b = divisorsum[a]
    c = divisorsum[b]
    if a == c and a != b:
        amicables.append(a)

print(amicables)
print(sum(amicables))
