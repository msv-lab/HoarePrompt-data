for _ in range(int(input())):
    (n, k) = map(int, stdin.readline().split())
    ans = [x for x in range(1, k // 2 + 1)] + [x for x in range(k + 1, n + 1)]
    print('%d\n%s' % (len(ans), ' '.join(map(str, ans))))