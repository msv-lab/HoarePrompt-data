d, k, a, b, t = map(int, input().split())
ans = float('inf')
for i in range((d-1)//k + 1):
    time = i * k * a + i * t
    time += (d - i * k) * b
    ans = min(ans, time)
print(ans)
