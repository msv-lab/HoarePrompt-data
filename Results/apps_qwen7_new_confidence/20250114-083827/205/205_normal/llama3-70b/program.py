a, b, x, y = map(int, input().split())
ans = 0
for w in range(x, a + 1, x):
    h = w * y // x
    if h <= b:
        ans += 1
print(ans)
