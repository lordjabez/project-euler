maxvalue = 201

denominations = [1, 2, 5, 10, 20, 50, 100, 200]

numways = [[None] * maxvalue] * len(denominations)

for i, d in enumerate(denominations):
    if i == 0:
        numways[i] = [1] * maxvalue
        continue
    for n in range(maxvalue):
        numways[i][n] = numways[i-1][n]
        if d <= n:
            numways[i][n] += numways[i][n-d]

print
for n, num in enumerate(numways):
    print denominations[n], num
