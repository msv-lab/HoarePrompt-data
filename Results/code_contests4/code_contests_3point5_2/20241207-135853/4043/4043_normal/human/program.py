import math

input = raw_input

def isprime(n):
    if n == 1: return True
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

A,B = map(int, input().split(" "))

a = []
for i in range(1,int(math.sqrt(A))+1):
    if A % i == 0:
        a.append(i)
        if i != A / i:
            a.append(A/i)

b = []
for i in range(1,int(math.sqrt(B))+1):
    if B % i == 0:
        b.append(i)
        if i != B / i:
            b.append(B/i)
c = 0
for i in a:
    if i in b and isprime(i):
        c += 1
print(c)
