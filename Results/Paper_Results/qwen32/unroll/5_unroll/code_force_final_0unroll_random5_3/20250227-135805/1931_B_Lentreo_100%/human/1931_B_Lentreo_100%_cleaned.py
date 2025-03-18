def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if total % n != 0:
        return 'NO'
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        if curr < 0:
            return 'NO'
    return 'YES'
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().strip().split()))
    print(func_1(nums))