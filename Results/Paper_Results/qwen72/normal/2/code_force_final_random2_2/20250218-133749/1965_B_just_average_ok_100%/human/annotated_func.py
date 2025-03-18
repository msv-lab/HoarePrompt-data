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
        
    #State: After all iterations of the loop, the list `nums` will contain the powers of 2 from \(2^0\) to \(2^{20}\) excluding \(2^{\text{idx}}\), followed by the values \(k - \text{nums}[\text{idx}]\), \(k + 1\), and \(k + \text{nums}[\text{idx}] + 1\). The variable `idx` will be the largest index such that `nums[idx] <= k`. The variable `i` will be the index where `nums[i] > k` or 20 if no such element exists. The length of `nums` will be 23. The values of `n` and `k` will be updated to the input values for each iteration.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it constructs a list `nums` containing powers of 2 from \(2^0\) to \(2^{20}\), modifies this list by removing one element and adding three new elements based on the value of `k`, and then prints the length of the modified list followed by the elements of the list. The function handles up to 1000 test cases, with each `n` and `k` satisfying the constraints \(2 \leq n \leq 10^6\) and \(1 \leq k \leq n\). After processing all test cases, the function has printed the results for each case, and the final state of the program is that all test cases have been processed and their results have been output.

