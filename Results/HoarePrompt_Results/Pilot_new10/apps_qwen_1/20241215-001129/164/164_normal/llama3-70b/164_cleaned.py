(n, k) = map(int, input().split())
s = input()
(g, t) = (-1, -1)
for i in range(n):
    if s[i] == 'G':
        g = i
    elif s[i] == 'T':
        t = i
if g == -1 or t == -1:
    print('NO')
elif abs(t - g) % k == 0 and all((s[(g + i * k) % n] != '#' for i in range(abs(t - g) // k + 1))):
    print('YES')
else:
    print('NO')