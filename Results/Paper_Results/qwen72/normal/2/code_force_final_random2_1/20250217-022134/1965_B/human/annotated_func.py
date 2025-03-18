#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: After all iterations of the loop, `t` is an integer such that \(1 \leq t \leq 1000\), and for each of the `t` test cases, `n` and `k` are integers such that \(2 \leq n \leq 10^6\) and \(1 \leq k \leq n\). For each test case, `nums` is a list initially containing the powers of 2 from \(2^0\) to \(2^{20}\). After processing each test case, `nums` is modified by removing the element \(2^{\text{idx}}\) (where `idx` is the index of the largest power of 2 in `nums` that is less than or equal to `k`, or -1 if no such element exists) and appending the elements `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`. The final state of `nums` for each test case will reflect these changes. The loop prints the length of the modified `nums` list and its contents for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves two integers `n` and `k`. For each test case, it modifies a list `nums` that initially contains the first 21 powers of 2 (from \(2^0\) to \(2^{20}\)). It finds the largest power of 2 in `nums` that is less than or equal to `k`, removes this power of 2 from `nums`, and appends three new elements: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1` (where `idx` is the index of the removed power of 2). The function then prints the length of the modified `nums` list followed by the elements of the list. The function does not return any value; it only prints the results for each test case.

