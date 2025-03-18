#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: For each test case, the loop outputs the length of the modified `nums` list, followed by the elements of the modified `nums` list. The modified `nums` list will have 23 elements, which are the original powers of 2 up to 2^20, with the element 2^idx removed, and the elements (k - 2^idx), (k + 1), and (k + 2^idx + 1) appended. The values of `t`, `n`, and `k` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` representing the number of test cases, and for each test case, it accepts two integers `n` and `k` where 2 <= n <= 10^6 and 1 <= k <= n. For each test case, the function modifies a list of powers of 2 (from 2^0 to 2^20) by removing the element 2^idx (where idx is the largest index such that 2^idx <= k) and appending the elements (k - 2^idx), (k + 1), and (k + 2^idx + 1). The function then prints the length of the modified list and the elements of the modified list. The values of `t`, `n`, and `k` remain unchanged after the function execution.

