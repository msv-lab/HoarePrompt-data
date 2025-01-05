import sys
import math

n,m,k = map(int, raw_input().split())
x = 1
y = 1

if k-n <= -1:
    print(y, k+1)
    sys.exit()
    
k -= n
t = k / (m - 1)
p = k % (m - 1)
y = n - t
x = 2 + p if t % 2 == 0 else m - p

print(int(math.ceil(y)), int(x))
print(y, x)