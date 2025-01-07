(n, k) = map(int, input().split())
w = 0
while n % 10 ** k != 0:
    w += 1
    n //= 10
print(w)