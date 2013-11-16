rng = range(2, 101)

nums = set()

for a in rng:
    for b in rng:
        n = a**b
        nums.add(n)

print len(nums)
