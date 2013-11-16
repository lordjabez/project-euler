def fibgen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

fibs = fibgen()

threshold = 10**10

for f, fib in enumerate(fibs):
    if fib > threshold:
        print(f+1, fib)
        break