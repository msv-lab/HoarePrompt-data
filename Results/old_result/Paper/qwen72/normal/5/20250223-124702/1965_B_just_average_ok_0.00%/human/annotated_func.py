#State of the program right berfore the function call: The function `func` does not take any input parameters, but based on the problem description, it is expected to handle multiple test cases where each test case consists of two integers n and k such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The function should be able to process up to 1000 test cases, and the sum of n over all test cases does not exceed 10^7.
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
        
    #State: The function processes each test case by modifying a list `nums` and printing the length of `nums` followed by the elements in `nums`. After all iterations of the loop, the variables `n`, `k`, and `nums` will have been used and modified for each test case, but the final state of these variables will be the state after the last test case has been processed. The list `nums` will contain four elements: the original powers of 2 up to 2^23, plus the three new elements added in the last test case, and minus the element that was removed. The length of `nums` will be 26 for the last test case. The specific values of `n`, `k`, and `nums` will depend on the input for the last test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of two integers `n` and `k` (where 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n). For each test case, it modifies a list `nums` that initially contains powers of 2 from 2^0 to 2^23. It then adds three new elements to `nums` and removes one element, and prints the length of `nums` followed by the elements in `nums`. After processing all test cases, the function has no return value, but the final state of `nums` will be modified based on the last test case, and the output will reflect the results for each test case.

