f = lambda: map(int, input().split())
n, r = f()
a = list(f())
ans = 0
last = -1
while last < n - 1:
    pos = -1
    i = n - 1
    while i > max(-1, last - r + 1):
        if a[i] == 1 and i - r <= last:
            pos = i
            break
        i -= 1
    if pos == -1:
        print(-1)
        exit()
    ans += 1
    last = pos + r - 1
print(ans)
