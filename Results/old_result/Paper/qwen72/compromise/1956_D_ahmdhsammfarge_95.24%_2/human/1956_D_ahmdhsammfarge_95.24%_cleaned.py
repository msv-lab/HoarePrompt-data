def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                (r, l) = [i, j]
                over_sum = sm
    return (r, l)

def func_2(r, l, ops: list):
    if r == l:
        ops.append([r + 1, l + 1])
        return
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)

def func_3(r, l, lst: list, ops: list):
    ops.append([r + 1, l + 1])
    if min(lst[r:l + 1]) == 0:
        ops.append([r + 1, l + 1])
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
input()
lst = list(map(int, input().split()))
ops = []
(r, l) = func_1(lst)
while r != l:
    lst = func_3(r, l, lst, ops)
    (r, l) = func_1(lst)
try:
    while True:
        i = lst.index(0) + 1
        lst[i - 1] = 1
        ops.append([i, i])
except ValueError:
    pass
print(sum(lst), len(ops))
for r in ops:
    print(*r)