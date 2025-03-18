#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: The number of elements in the list `nums` after processing each test case, followed by the elements themselves. The list `nums` will contain up to 23 unique integers for each test case, which are derived from the value of `k` and some powers of 2. Specifically, the list will include the following elements: \(2^{0}\) to \(2^{20}\), the value of `k`, `k-2^idx`, `k+1`, and `k+2^idx+1`, where `idx` is the index just before the first power of 2 greater than `k`. The exact elements and their count depend on the specific values of `n` and `k` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: the number of test cases \(t\), and for each test case, two integers \(n\) and \(k\). For each test case, it generates a list `nums` containing up to 23 unique integers derived from \(k\) and some powers of 2. Specifically, the list includes the values \(2^0\) to \(2^{20}\), the value of \(k\), \(k - 2^{idx}\), \(k + 1\), and \(k + 2^{idx} + 1\), where \(idx\) is the index just before the first power of 2 greater than \(k\). The function then prints the number of elements in `nums` followed by the elements themselves.

