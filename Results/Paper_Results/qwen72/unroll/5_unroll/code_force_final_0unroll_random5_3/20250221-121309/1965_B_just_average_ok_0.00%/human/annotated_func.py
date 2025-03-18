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
        
    #State: For each test case, the loop prints the length of the modified `nums` list and the elements of the modified `nums` list. The `nums` list initially contains powers of 2 from \(2^0\) to \(2^{23}\). After the loop, the list `nums` will have the same length as initially (24 elements), but the element \(2^{\text{idx}}\) will be removed and replaced by `k - 2^{\text{idx}}`, `k + 1`, and `k + 2^{\text{idx}} + 1`. The variable `t` will be unchanged, and `n` and `k` will be reset for the next iteration if there are more test cases.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads two integers `n` and `k` from input, modifies a list `nums` that initially contains the first 24 powers of 2, and prints the length of the modified `nums` list followed by the elements of the list. The modification involves removing the largest power of 2 less than or equal to `k` from `nums` and adding three new elements: `k - 2^idx`, `k + 1`, and `k + 2^idx + 1`, where `2^idx` is the removed power of 2. The function does not return any value; it only prints the results for each test case. The variable `t` (number of test cases) remains unchanged throughout the function's execution.

