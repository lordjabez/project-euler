#rng = range(2, 10000)
rng = range(2, (9**5)*6+1)

nums = []

for n in rng:
    digits = (int(c) for c in str(n))
    sum5 = sum(n**5 for n in digits)
    if sum5 == n:
        nums.append(n)

print(sum(nums))

# Closed form: 16/3 n^3 + 10 n^2 + 26/3 n + 1