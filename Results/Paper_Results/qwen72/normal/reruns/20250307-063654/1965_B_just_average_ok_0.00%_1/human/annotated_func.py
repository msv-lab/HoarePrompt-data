#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case contains two integers n and k such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The number of test cases t is an integer such that 1 ≤ t ≤ 1000, and the sum of n over all test cases does not exceed 10^7.
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
        
    #State: The loop has executed for all test cases. For each test case, `nums` is a list of powers of 2 from \(2^0\) to \(2^{23}\) excluding \(2^{\text{idx}}\), followed by the values \(k - 2^{\text{idx}}\), \(k + 1\), and \(k + 2^{\text{idx}} + 1\). The length of `nums` is printed, followed by the elements of `nums`. The variables `_`, `n`, and `k` have been updated for each test case, and `idx` has been recalculated for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves two integers `n` and `k` within specified constraints. For each test case, the function generates a modified list `nums` that initially contains powers of 2 from \(2^0\) to \(2^{23}\). It then updates this list by removing \(2^{\text{idx}}\) (where `idx` is the largest integer such that \(2^{\text{idx}} \leq k\)), and adding the values \(k - 2^{\text{idx}}\), \(k + 1\), and \(k + 2^{\text{idx}} + 1\). The function prints the length of the updated `nums` list and the elements of the list. After processing all test cases, the function has no return value, but it has printed the results for each test case.

