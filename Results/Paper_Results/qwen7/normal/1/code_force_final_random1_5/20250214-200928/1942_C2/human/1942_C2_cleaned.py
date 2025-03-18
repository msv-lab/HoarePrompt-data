tt = int(input())
for ii in range(tt):
    (n, x, y) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = x + y - 2
    tmp = []
    for i in range(1, len(a)):
        if a[i] - a[i - 1] == 2:
            ans += 1
        elif (a[i] - a[i - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
            tmp.append((a[i] - a[i - 1]) // 2)
            ans += (a[i] - a[i - 1]) // 2
            y -= (a[i] - a[i - 1]) // 2 - 1
    if a[0] + n - a[len(a) - 1] == 2:
        ans += 1
    elif (a[0] + n - a[len(a) - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
        tmp.append((a[0] + n - a[len(a) - 1]) // 2)
        ans += (a[i] - a[i - 1]) // 2
        y -= (a[i] - a[i - 1]) // 2 - 1
    ans += y
    print(min(ans, n - 2))