for _ in range(int(input())):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    if len(set(a)) == 1 and len(set(c)) == 1 and (a[0] == c[0]):
        print(0)
        continue
    a.sort()
    c.sort(reverse=True)
    if len(a) == 1:
        print(max(abs(a[0] - max(c)), abs(a[0] - min(c))))
        continue
    (i, ans) = (0, 0)
    while i < len(a) // 2:
        ans += abs(a[i] - c[i])
        i += 1
    j = len(c) - len(a) + i
    while i < len(a):
        ans += max(abs(a[i] - c[i]), abs(a[i] - c[j]))
        i += 1
        j += 1
    print(ans)