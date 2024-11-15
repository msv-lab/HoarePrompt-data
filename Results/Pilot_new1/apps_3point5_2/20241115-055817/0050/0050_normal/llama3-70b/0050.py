n, m, r = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(int, input().split()))

s.sort()
b.sort(reverse=True)

shares = 0
for i in range(n):
    if r >= s[i]:
        shares += r // s[i]
        r %= s[i]
    else:
        break

for i in range(m):
    if shares > 0:
        r += shares * b[i]
        shares = 0
    else:
        break

print(r)
