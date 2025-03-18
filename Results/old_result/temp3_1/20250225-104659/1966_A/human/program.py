def func():
    for _ in range(int(input())):
        (n, k) = map(int, input().split())
        a = list(map(int, input().split()))
        h = {}
        ans = n
        for i in a:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] >= k:
                ams = k - 1
        print(ans)

