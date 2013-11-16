solutions = set()

for n in range(1000000):
    strn = str(n)
    if strn == strn[::-1]:
        binn = bin(n)[2:]
        if binn == binn[::-1]:
            solutions.add(n)

print(sum(solutions))
