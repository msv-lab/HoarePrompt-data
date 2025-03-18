#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: The number of elements in `nums` list will vary based on the value of `k` for each test case. For each test case, `nums` will contain 5 elements: three fixed elements `[1, 2, 4, ..., 16777216]` (which are powers of 2 up to \(2^{24}\)), the calculated element `k - nums[idx]`, and `k + 1`. After removing `1 << idx`, the list will have 5 elements. The exact values will depend on the specific values of `n` and `k` for each test case, but the length of `nums` will always be 5.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \(n\) and \(k\). It then constructs a list `nums` containing five specific elements: three fixed elements which are powers of 2 up to \(2^{24}\), a dynamically calculated element based on \(k\), and two additional elements derived from \(k\). After constructing the list, it removes one of the fixed elements and prints the length of the resulting list followed by its elements. This process is repeated for each test case provided.

