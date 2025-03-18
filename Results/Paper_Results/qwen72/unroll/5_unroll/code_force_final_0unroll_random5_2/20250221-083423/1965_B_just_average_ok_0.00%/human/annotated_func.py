#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: The loop modifies the `nums` list and prints the length of the modified list followed by the elements of the list for each iteration. The variables `n` and `k` are read from input for each iteration and are not affected by the loop body. The state of `n` and `k` remains as integers such that 2 <= n <= 10^6 and 1 <= k <= n.
#Overall this is what the function does:The function `func` reads multiple pairs of integers `n` and `k` from the standard input, where each pair satisfies `2 <= n <= 10^6` and `1 <= k <= n`. For each pair, it modifies a list `nums` by adding and removing specific elements based on the value of `k`. It then prints the length of the modified `nums` list followed by the elements of the list. The function does not return any value. After the function concludes, the state of `n` and `k` remains unchanged for each iteration, and the `nums` list is reset for the next iteration.

