input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
number_testcase = int(input().decode())

def func_1():
    global skipper, acc
    pre_acc = [0] * n
    acc = [0] * n
    skipper = [None] * n
    starts_to_stop = dict()
    for (idx, loc) in enumerate(catsLines):
        (l, r) = loc
        l -= 1
        r -= 1
        pre_acc[l] += 1
        if r + 1 != n:
            pre_acc[r + 1] -= 1
        if l not in starts_to_stop:
            starts_to_stop[l] = r
        starts_to_stop[l] = max(starts_to_stop[l], r)
    currentMax = None
    for idx in range(n):
        if currentMax == idx:
            currentMax = None
        if idx in starts_to_stop:
            currentMax = starts_to_stop[idx] if currentMax is None else max(currentMax, starts_to_stop[idx])
        if currentMax is not None:
            skipper[idx] = currentMax + 1
        else:
            skipper[idx] = idx + 1
    for (idx, val) in enumerate(pre_acc):
        acc[idx] = pre_acc[idx] + (acc[idx - 1] if idx > 0 else 0)

def func_2():
    global catsLines, n, m
    (n, m) = list(map(int, input().decode().split()))
    n += 2
    catsLines = [tuple(map(int, input().decode().split())) for _ in range(m)]
    func_1()
    M = [0] * n
    maxM = [0] * n
    for i in range(n - 3, -1, -1):
        M[i] = acc[i] + maxM[skipper[i]]
        maxM[i] = max(M[i], maxM[i + 1])
    print(max(M))
for _ in range(number_testcase):
    func_2()