num = 600851475143

for n in range(2,10000):
    if all(n % i != 0 for i in range(2,n)):
        while num % n == 0:
            num //= n
            print(n, num)

#primes
