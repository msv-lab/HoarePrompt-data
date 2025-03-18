from math import gcd
 
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
 
def calculate_lcm(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result
 
t = int(input())
for _ in range(t):
    n=int(input())
    k=list(map(int, input().split()))
    m=calculate_lcm(k)
    c=[]
    for i in range(n):
        c.append(m//k[i])
    if sum(c)>=m:
        print(-1)
        continue
    for i in range(n):
        print(c[i], end=' ')
    print('\n', end='')