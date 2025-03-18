T = int(input())
for _ in range(T):
    (n, k) = map(int, input().split())
    lst = list(map(int, input().split()))
    lft = lst[:n]
    rgt = lst[n:]
    ldb = []
    rdb = []
    sng = []
    lft.sort()
    rgt.sort()
    for i in range(1, n):
        if lft[i] == lft[i - 1]:
            ldb.append(lft[i])
        elif i < n - 1 and lft[i] != lft[i + 1]:
            sng.append(lft[i])
    for i in range(1, n):
        if rgt[i] == rgt[i - 1]:
            rdb.append(rgt[i])
    sz = 0
    for elem in ldb:
        if sz >= k:
            break
        if k - sz >= 2:
            print(elem, elem, end=' ')
            sz += 2
    for elem in sng:
        if sz >= k:
            break
        print(elem, end=' ')
        sz += 1
    print()
    sz = 0
    for elem in rdb:
        if sz >= k:
            break
        if k - sz >= 2:
            print(elem, elem, end=' ')
            sz += 2
    for elem in sng:
        if sz >= k:
            break
        print(elem, end=' ')
        sz += 1