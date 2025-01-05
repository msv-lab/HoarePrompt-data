# 需要反推，正推会tle
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()
    left, right = 0, n - 1
    for c in s[:-1]:
        if c == 'L':
            left += 1
        else:
            right -= 1
    mid = []
    ans = a[left] % m               # 最后停留的位置
    mid.append(ans)
    for i in range(n - 2, -1, -1):  # 反推
        if s[i] == 'L':
            left -= 1
            ans *= a[left]
        else:
            right += 1
            ans *= a[right]
        ans %= m
        mid.append(ans)
    print(' '.join(map(str, mid[::-1])))