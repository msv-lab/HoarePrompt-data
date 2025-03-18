T = int(input())

def func_1(n, k, nums):
    if k >= sum(nums):
        return n
    (a, b) = (math.ceil(k / 2), k // 2)
    ans = 0
    s_a = 0
    s_b = 0
    for i in range(n):
        s_a += nums[i]
        s_b += nums[n - i - 1]
        if s_a <= a:
            ans += 1
        if s_b <= b:
            ans += 1
    return ans
for _ in range(T):
    (n, k) = list(map(int, input().split(' ')))
    nums = list(map(int, input().split(' ')))
    ans = func_1(n, k, nums)
    print(ans)