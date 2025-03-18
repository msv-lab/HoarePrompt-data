def func_1(n, k):
    nums = [0] * n
    for i in range(n):
        nums[i] = (1 << k.bit_length() - 1) - 1
        k -= nums[i]
    nums[-1] += k
    return nums
t = int(input())
results = []
for _ in range(t):
    (n, k) = map(int, input().split())
    result = func_1(n, k)
    results.append(' '.join(map(str, result)))
print('\n'.join(results))