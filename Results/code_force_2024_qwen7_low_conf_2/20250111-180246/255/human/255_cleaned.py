def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    pref = [arr[i] for i in range(n)]
    for i in range(1, n):
        pref[i] += pref[i - 1]
    ind = -1
    ans = [10 ** 9 for i in range(n)]
    for i in range(n):
        curr = pref[i] - 2 * arr[i]
        ind1 = bisect.bisect_left(pref, curr)
        ind = min(ind, ind1)
        if ind >= 0 and curr > 0:
            ans[i] = i - ind
        if i - 1 >= 0 and arr[i] != arr[i - 1]:
            if arr[i] < arr[i - 1]:
                ans[i] = 1
                ind = i
    ind = n
    for i in range(n - 1, -1, -1):
        curr = pref[i] + arr[i] + 1
        ind1 = bisect.bisect_left(pref, curr)
        ind = max(ind, ind1)
        if ind < n and curr <= pref[-1]:
            ans[i] = min(ans[i], ind - i)
        if i + 1 < n and arr[i] != arr[i + 1]:
            if arr[i] < arr[i + 1]:
                ans[i] = 1
                ind = i
    for i in range(n):
        if ans[i] == 10 ** 9:
            ans[i] = -1
    print(*ans)
for _ in range(int(input())):
    func_1()