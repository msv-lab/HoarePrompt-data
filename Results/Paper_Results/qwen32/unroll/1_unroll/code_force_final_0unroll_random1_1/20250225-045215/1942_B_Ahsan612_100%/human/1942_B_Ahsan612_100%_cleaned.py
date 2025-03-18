for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    res = [None] * n
    mex = n
    for i in range(len(ar) - 1, -1, -1):
        res[i] = mex - ar[i]
        if mex > mex - ar[i]:
            mex = mex - ar[i]
    print(' '.join((str(x) for x in res)))