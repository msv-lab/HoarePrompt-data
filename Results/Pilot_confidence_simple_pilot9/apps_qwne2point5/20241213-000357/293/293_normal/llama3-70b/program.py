h, n = map(int, input().split())
ans = 0
while n > 1:
    if n % 2 == 0:
        ans += (n // 2) - 1
    else:
        ans += n // 2
    n //= 2
print(ans)
