import math

n, k = raw_input().split()
n, k = int(n), int(k)
arr = map(int,raw_input().split())
count = 0.0

for i in range(n):
    if arr[i] + k <= 5:
        count += 1.0

print(int(math.floor(count / 3)))