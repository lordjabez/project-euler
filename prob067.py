triangle = []

with open('triangle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        triangle.append(list(map(int, line.split())))
        

triangle.reverse()

print(triangle)

for n, row in enumerate(triangle):
    if n == 0:
        continue
    for k, num in enumerate(row):
        row[k] += max(triangle[n-1][k], triangle[n-1][k+1])

print(triangle)
