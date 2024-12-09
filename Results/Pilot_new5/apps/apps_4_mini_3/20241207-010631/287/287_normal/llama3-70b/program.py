n = int(input())
res = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        res += 2
    if i * i == n:
        res -= 1
print(res)
