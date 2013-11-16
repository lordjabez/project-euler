count = 0

for n in range(1,1000000):
    if all(n % i != 0 for i in range(2,n)):
        count += 1
        print(n, count)
        if count > 10010:
            break
