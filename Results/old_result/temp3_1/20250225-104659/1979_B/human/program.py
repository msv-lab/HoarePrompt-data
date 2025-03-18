def func():
    t = int(input())
    for _ in range(t):
        (x, y) = map(int, input().split())
        (l1, l2) = ([], [])
        while x:
            l1.append(x % 2)
            x //= 2
        while y:
            l2.append(y % 2)
            y //= 2
        if len(l2) < len(l1):
            l2.append(0)
        elif len(l1) < len(l2):
            l1.append(0)
        n = len(l1)
        if len(l2) < len(l1):
            n = len(l2)
        cnt = 0
        for i in range(n):
            if l1[i] == l2[i]:
                cnt += 1
            else:
                break
        print(2 ** cnt)

