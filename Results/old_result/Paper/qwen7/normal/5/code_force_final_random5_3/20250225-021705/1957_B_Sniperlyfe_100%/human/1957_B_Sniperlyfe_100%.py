def max_or_sum(n, k):
    nums = [0] * n
    nums[0] = (1 << (k.bit_length() - 1)) - 1
    k -= nums[0]
    
    for i in range(1, n):
        if k > 0:
            nums[i] = min(nums[0] + 1, k)
            k -= nums[i]
    
    nums[0] += k
    
    return nums
 
t = int(input())
results = []
 
for _ in range(t):
    n, k = map(int, input().split())
    result = max_or_sum(n, k)
    results.append(" ".join(map(str, result)))
 
print("\n".join(results))