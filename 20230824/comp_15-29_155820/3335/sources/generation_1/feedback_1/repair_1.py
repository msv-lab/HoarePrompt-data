import math

n = int(input())

count = 0

for a in range(1, n):
    for b in range(a, n):
        c = (a**2 + b**2) % n
        if c*c % n == (a**2 + b**2) % n:
            count += 1

print(count)