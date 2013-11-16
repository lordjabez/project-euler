size = 1001
nums = (size - 1) * 2

v = 1
s = 1
print(v, s)

for i in range(nums):
    v += (i // 4) * 2 + 2
    s += v
    
print(v, s)



#3x3 = 25
#5x5 = 101



#n + n + k + n + 2*k + n + 3*k
#4*n + 6*k

