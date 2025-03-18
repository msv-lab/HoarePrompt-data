def func():
    for _ in range(int(input())):
        (x, n) = map(int, input().split())
        k = x // n
        ans = 1
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        print(ans)

