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
        
    #State: After the loop executes all iterations, `t` is an integer such that 1 <= t <= 1000, `_` is `t - 1`, `nums` is a list of integers where each element is \(2^i\) for \(i\) in the range 0 to 23, excluding the elements \(2^{\text{idx}}\) for each test case, and includes additional elements `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1` for each test case, where `idx` is the smallest integer such that \(2^{\text{idx}} > k\) for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` from the input, which represents the number of test cases, with 1 <= t <= 1000. For each test case, it reads two integers `n` and `k` from the input, where 2 <= n <= 10^6 and 1 <= k <= n. The function then modifies a list `nums` that initially contains powers of 2 from 2^0 to 2^23. It adds three new elements to `nums`: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`, where `idx` is the largest index such that 2^idx <= k. It removes the element 2^idx from `nums`. Finally, it prints the length of the modified `nums` list and the elements of the list for each test case. The function does not return any value.

