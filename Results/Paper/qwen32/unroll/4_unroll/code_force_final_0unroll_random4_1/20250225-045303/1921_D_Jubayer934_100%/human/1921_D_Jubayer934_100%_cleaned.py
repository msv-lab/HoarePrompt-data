for _ in range(int(input())):
    (n, m) = map(int, input().split())
    temp = -1
    ans = []
    a = sorted(map(int, input().split()))[:n]
    b = sorted(map(int, input().split()), reverse=True)[:m]
    for i in range(n):
        if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
            temp = i
            break
        ans.append(abs(a[i] - b[i]))
    if temp != -1:
        for i in range(temp, n):
            ans.append(abs(a[i] - b[-(n - i)]))
    print(sum(ans))