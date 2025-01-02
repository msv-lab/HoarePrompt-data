a = dict()
for i in range(-10, 11):
    a[i] = 0
n = input()
t = map(int, raw_input().split())
for i in range(n):
    a[t[i]] += 1
ans = 0
for i in range(-10, 0):
    ans += a[i] * a[-i]
ans += a[0] * (a[0] - 1) / 2
print(ans)