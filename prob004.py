threedigit = range(100, 1000)

palindromes = [int(str(i) + str(i)[::-1]) for i in range(100, 1000)]

largest = 0

for m in range(100, 1000):
    for n in range(m, 1000):
        x = m * n
        if x in palindromes and x > largest:
            largest = x
            print('{0} * {1} = {2}'.format(m, n, x))
    