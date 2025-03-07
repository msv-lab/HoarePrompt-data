def func_1(a, x):
    if x < 0:
        return -1
    inx = bl(a, x)
    if a[inx] == x:
        return inx + 1
    return inx

def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
    for i in a:
        left.append(left[-1] + i)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            ans[i] = 1
            continue
        x = left[i] - a[i] - 1
        inx = func_1(left, x)
        inx2 = last[i - 1]
        if inx2 < inx:
            inx = inx2
        if inx < 0:
            continue
        ans[i] = i + 1 - inx
    return ans
for iiii in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = func_2(a, n)
    ans2 = func_2(a[::-1], n)
    ans2 = ans2[::-1]
    for i in range(n):
        if ans[i] == -1 or ans2[i] == -1:
            ans[i] = max(ans[i], ans2[i])
        else:
            ans[i] = min(ans[i], ans2[i])
    print(*ans)