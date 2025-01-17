def getMaxable(lst):
    rls = []
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j+1:]) + (j - i + 1) ** 2
            if (dif := sm - over_sum) > 0:
                for rl in rls:
                    if i > rl[-2] + 1:
                        rls.append(rl + [i, j, dif])
                rls.append([i, j, dif])
    sums = [sum(rl[2::3]) for rl in rls]
    return rls[sums.index(max(sums))] if len(sums) > 0 else []


def addOps(r, l, ops: list):
    if r == l:
        ops.append([r + 1, l + 1])
        return
    addOps(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    addOps(r, l - 1, ops)


def doOps(r, l, lst: list, ops: list):
    ops.append([r + 1, l + 1])
    if lst[r:l + 1].__contains__(0):
        ops.append([r + 1, l + 1])
    ops.append([r + 1, r + 1])
    addOps(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst


input()
lst = list(map(int, input().split()))

ops = []
rls = getMaxable(lst)
while rls:
    for i in range(0, len(rls), 3):
        r, l = rls[i:i+2]
        lst = doOps(r, l, lst, ops)
    rls = getMaxable(lst)

print(sum(lst), len(ops))
for r in ops:
    print(*r)
    