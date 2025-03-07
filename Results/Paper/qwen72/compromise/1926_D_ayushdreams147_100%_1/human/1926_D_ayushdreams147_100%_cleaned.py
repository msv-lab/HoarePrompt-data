def func_1(n, a):
    res = 0
    count = {}
    for num in a:
        if num not in count:
            count[(1 << 31) - 1 ^ num] = count.get((1 << 31) - 1 ^ num, 0) + 1
            res += 1
        else:
            count[num] -= 1
            if count[num] == 0:
                del count[num]
    return res
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(func_1(n, a))