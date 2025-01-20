(n, k) = map(int, input().split())

def func_1(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x - 1

def func_2(x):
    res = [x]
    while x != 1:
        x = func_1(x)
        res.append(x)
    return res
count = {}
for i in range(1, n + 1):
    for j in func_2(i):
        if j not in count:
            count[j] = 0
        count[j] += 1
max_y = 0
for (y, cnt) in count.items():
    if cnt >= k:
        max_y = max(max_y, y)
print(max_y)