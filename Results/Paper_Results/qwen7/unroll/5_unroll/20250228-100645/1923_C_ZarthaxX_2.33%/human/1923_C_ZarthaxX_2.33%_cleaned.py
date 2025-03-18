def func_1():
    (n, q) = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [0 for i in range(n + 1)]
    sum = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        sum[i] = sum[i - 1] + nums[i - 1] - 1
    for _ in range(q):
        (l, r) = map(int, input().split(' '))
        if l == r:
            print('NO')
            continue
        onesInRange = ones[r] - ones[l - 1]
        sumInRange = sum[r] - sum[l - 1]
        if 2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange:
            print('YES')
        else:
            print('NO')
testCases = int(input())
for i in range(testCases):
    func_1()