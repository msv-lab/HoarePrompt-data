n = int(raw_input())
a = map(int, raw_input().split())
a = sorted(a)
x = a[2]
ans = 1
for i in xrange(3, len(a)):
    if a[i] == x:
        ans += 1
    else:
        break
print(ans)