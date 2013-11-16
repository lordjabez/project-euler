total = 1000000

length = [0] * total

length[1] = 1

for s in range(2, total):
    if not length[s]:
        n = s
        count = 0
        while True:
            count += 1
            if n % 2:
                n = 3 * n + 1
            else:
                n = n // 2
            if n < total and length[n]:
                count += length[n]
                break
            else:
                count += 1
        length[s] = count

maxlength = max(length)

print(maxlength)
print(length.index(maxlength))
