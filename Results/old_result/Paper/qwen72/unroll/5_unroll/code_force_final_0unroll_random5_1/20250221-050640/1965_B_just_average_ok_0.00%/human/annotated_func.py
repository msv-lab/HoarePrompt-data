#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: For each test case, the loop prints the length of the modified list `nums` and the elements of the modified list `nums`. The length of `nums` is 25, and the elements are the powers of 2 from 1 to 2^23, excluding 2^idx, and including k - 2^idx, k + 1, and k + 2^idx + 1. The variables `t`, `n`, and `k` remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k` where 2 <= n <= 10^6 and 1 <= k <= n. For each test case, it modifies a list `nums` that initially contains the powers of 2 from 1 to 2^23. It then prints the length of the modified list `nums` (which is 25) and the elements of the modified list. The elements of `nums` are the powers of 2 from 1 to 2^23, excluding 2^idx, and including k - 2^idx, k + 1, and k + 2^idx + 1, where `idx` is the largest integer such that 2^idx <= k. The variables `t`, `n`, and `k` remain unchanged after the function execution.

