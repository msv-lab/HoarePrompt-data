import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def count_ordered_pairs(n, m):
    cnt = 0
    
    for i in range(1, m):
        x = n - (i * i - i)
        y = i * i
        cnt = cnt + (x//y) + (i > 1)
 
    if cnt == 0:
        return 1
    return cnt
 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = count_ordered_pairs(n, m)
    print(result)