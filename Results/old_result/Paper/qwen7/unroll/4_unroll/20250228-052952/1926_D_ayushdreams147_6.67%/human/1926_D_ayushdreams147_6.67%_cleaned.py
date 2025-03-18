def func_1(n, a):
    res = 0
    count = {}
    for num in a:
        if num not in count:
            count[num ^ (1 << 31) - 1] = count.get(num ^ (1 << 31) - 1, 0) + 1
            res += 1
        else:
            count[num] -= 1
    return res
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(func_1(n, a))