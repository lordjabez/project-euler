def fibs():
    a, b = 2, 3
    while True:
        yield a
        a, b = a + 2 * b, 2 * a + 3 * b
        if a > 4000000:
            break        

fib = fibs()

for f in fib:
    print(f)

#x = sum(fib)
#print(x)
