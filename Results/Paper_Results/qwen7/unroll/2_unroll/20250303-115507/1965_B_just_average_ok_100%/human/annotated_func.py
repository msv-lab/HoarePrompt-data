#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        nums = [(1 << i) for i in range(21)]
        
        idx = -1
        
        for i in range(len(nums)):
            if nums[i] > k:
                idx = i - 1
                break
        
        nums.append(k - nums[idx])
        
        nums.append(k + 1)
        
        nums.append(k + nums[idx] + 1)
        
        nums.remove(1 << idx)
        
        print(len(nums))
        
        print(*nums)
        
    #State: Output State: The number of elements in the list `nums` after processing each test case, followed by the elements in the list `nums`. The list `nums` will contain up to 24 unique elements, which are derived from the value of `k` and the fixed values \(1 \ll i\) for \(i\) in range(21). The exact elements in `nums` depend on the value of `k` for each test case, but it will always include \(k\), \(k-2^j\) where \(2^j\) is the largest power of 2 less than or equal to \(k\), \(k+1\), and \(k+2^j+1\), with one element removed based on the value of `k`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \(n\) and \(k\). It then constructs a list `nums` containing up to 24 unique elements derived from \(k\) and fixed values of \(2^i\) for \(i\) in range(21). Specifically, it includes \(k\), \(k - 2^j\) (where \(2^j\) is the largest power of 2 less than or equal to \(k\)), \(k + 1\), and \(k + 2^j + 1\), and removes one element based on the value of \(k\). Finally, it prints the number of elements in `nums` followed by the elements themselves for each test case.

