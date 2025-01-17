def func_1():
    input = sys.stdin.read
    data = input().split()
    ans1 = [8]
    ans2 = [[[2, 6, 8], [3, 5, 7]]]
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        if n in ans1:
            ans = ans2[ans1.index(n)]
            results.append(f'{len(ans)}')
            for x in ans:
                results.append(' '.join(map(str, x)))
            continue
        ans = []
        pos = 0
        ost = []
        for i in range(3, n - 1, 4):
            if i > n // 2 - 2:
                ans.append([i, i + 1, i + 2])
                pos = i + 2
        for i in range(pos + 1, n + 1):
            if (i % 2 != 0 or i % 4 == 0) and i > n // 2:
                ost.append(i)
        per = n
        if (n - 1) % 4 == 2:
            per = n - 1
        elif (n - 2) % 4 == 2:
            per = n - 2
        elif (n - 3) % 4 == 2:
            per = n - 3
        for i in range(per, n // 2, -12):
            if i > n // 2:
                if i > 8:
                    ans.append([i, i - 4, i - 8])
                else:
                    ost.append(i)
        if len(ost) == 1:
            ans.append([1, 2, ost[0]])
        elif len(ost) == 2:
            ans.append([1, ost[1], ost[0]])
        elif len(ost) == 3:
            ans.append([ost[0], ost[1], ost[2]])
        elif len(ost) == 4:
            ans.append([1, ost[0], ost[1]])
            ans.append([2, ost[2], ost[3]])
        results.append(f'{len(ans)}')
        for x in ans:
            results.append(' '.join(map(str, x)))
    sys.stdout.write('\n'.join(results) + '\n')