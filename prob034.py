import math

factorial = [math.factorial(i) for i in range(10)]

solutions = []

for n in range(3, 2540161):
    if n == sum(factorial[int(d)] for d in str(n)):
        print(n)
        solutions.append(n)
    
print(solutions)
    