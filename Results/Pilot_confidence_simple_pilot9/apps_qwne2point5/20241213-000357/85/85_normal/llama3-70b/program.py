n = int(input())
ans = 0
for i in range(1, n // 2 + 1):
    if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
        ans += 1
print(ans)
