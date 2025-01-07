n, k = map(int, input().split())
x = 10 ** k
while n % x != 0:
    n += 1
print(n)
