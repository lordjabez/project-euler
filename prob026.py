repeats = [0]

largestindex = 0
largestvalue = 0

for n in range(1, 1000):
    d = 1
    count = 0
    dvalues = {1: 0}
    diff = None
    while diff is None:
        while d < n:
            d *= 10
            count += 1
            #print(d, count, dvalues)
            if d in dvalues:
                diff = count - dvalues[d] if d else 0
                break
            dvalues[d] = count
        d = (d % n) * 10
        count += 1
        #print(d, count, dvalues)
        if d in dvalues:
            diff = count - dvalues[d] if d else 0
        dvalues[d] = count
    if diff > largestvalue:
        largestindex = n
        largestvalue = diff

print(largestindex)
print(largestvalue)