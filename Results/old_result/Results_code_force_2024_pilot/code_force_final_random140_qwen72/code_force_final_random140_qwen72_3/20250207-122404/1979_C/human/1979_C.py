from math import gcd
 
def calculate_hcf(numbers):
    hcf = numbers[0]
    for num in numbers[1:]:
        hcf = gcd(hcf, num)
    return hcf
 
t = int(input())
for _ in range(t):
    n=int(input())
    k=list(map(int, input().split()))
    m=1
    for i in range(n):
        m=m*k[i]
    c=[]
    for i in range(n):
        c.append(int(m/k[i]))
    hcf=calculate_hcf(c)
    for i in range(n):
        c[i]=int(c[i]/hcf)
    if sum(c)>=m:
        print(-1)
    else:
        for i in range(n):
            print(c[i], end=' ')
        print('')