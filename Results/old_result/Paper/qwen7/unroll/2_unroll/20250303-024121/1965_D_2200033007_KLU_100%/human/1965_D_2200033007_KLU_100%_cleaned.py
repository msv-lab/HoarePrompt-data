def func_1(a):
    cts = []
    for i in range(len(a)):
        sm = 0
        for j in range(i, len(a)):
            sm = sm + a[j]
            cts.append(sm)
    cts.sort()
    return cts

def func_2(cts):
    odds = []
    for ct in cts:
        if len(odds) > 0 and ct == odds[-1]:
            odds.pop()
        else:
            odds.append(ct)
    return odds

def func_3(odds, n):
    a = [0] * n
    prev = 0
    idx = (n - 1) // 2
    for x in odds:
        if idx == n - 1 - idx:
            a[idx] = x
        else:
            a[idx] = (x - prev) // 2
            a[n - 1 - idx] = (x - prev) // 2
        prev = x
        idx = idx - 1
    return a

def func_4(bigList, smallList):
    while len(smallList) > 0 and bigList[-1] == smallList[-1]:
        bigList.pop()
        smallList.pop()
    return bigList[-1]
t = int(input())
for tc in range(t):
    n = int(input())
    subarraySums = list(map(int, input().split()))
    subarraySums.sort()
    odds = func_2(subarraySums)
    missingSum = -1
    if len(odds) > (n + 1) // 2:
        oddvals = []
        evenvals = []
        for x in odds:
            if x % 2 == 1:
                oddvals.append(x)
            else:
                evenvals.append(x)
        if len(evenvals) > 0 and len(oddvals) > 0:
            missingSum = evenvals[0] if len(evenvals) == 1 else oddvals[0]
        else:
            b = func_3(odds, n + 2)
            bSums = func_1(b)
            y = bSums[-1]
            x = func_4(bSums, subarraySums)
            missingSum = 2 * x - y
    else:
        b = func_3(odds, n - 2)
        bSums = func_1(b)
        y = bSums[-1]
        x = func_4(subarraySums, bSums)
        missingSum = 2 * x - y
    odds.append(missingSum)
    odds.sort()
    odds = func_2(odds)
    ans = func_3(odds, n)
    print(*ans)