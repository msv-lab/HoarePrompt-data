#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        nums = [(1 << i) for i in range(24)]
        
        idx = 0
        
        while k >= 1 << idx:
            idx += 1
        
        idx -= 1
        
        nums.append(k - nums[idx])
        
        nums.append(k + 1)
        
        nums.append(k + nums[idx] + 1)
        
        nums.remove(1 << idx)
        
        print(len(nums))
        
        print(*nums)
        
    #State: t is a positive integer such that \(1 \leq t \leq 1000\), `_` is 999, `n` is an input integer, `k` must be at least \(2^{23} = 8388608\), `nums` is a list containing the values `[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]` with the element `16777216` removed, `idx` is 23, and the numbers `k - 8388608`, `k + 1 + nums[23] + 1`, and `k + 1` are appended to the list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t, n, and k. For each test case, it constructs a list of specific integers based on k and prints the length of this list followed by the list itself. The list contains predefined values, the value of k adjusted in certain ways, and some removed values.

