#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: The loop will execute for each test case provided by the user. After all iterations, `num_tests` will be the total number of test cases processed, which is a positive integer such that 1 <= num_tests <= 1000. For each test case, `n` will be the integer obtained from the first input split, and `k` will be an integer within the range 2 <= k <= n. The variable `nums` will be a list containing specific integers based on the value of `k` for each test case. Specifically, `nums` will include the powers of 2 up to the largest power of 2 less than or equal to `k`, plus three additional elements: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`. After removing the largest power of 2 from the list, `nums` will contain exactly 25 elements. The variable `idx` will be set to the index of the largest power of 2 removed from the list, which will vary depending on the value of `k`.
    #
    #In summary, after all iterations of the loop, the output state will reflect the processing of all test cases, with `num_tests` indicating the total number of cases, `n` and `k` representing the parameters for each case, and `nums` being the final list of 25 integers for each case as described above.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n and k. For each test case, it generates a list `nums` containing 25 specific integers based on the value of k. The list includes powers of 2 up to the largest power of 2 less than or equal to k, plus three additional elements derived from k. After processing all test cases, it prints the length of `nums` and the elements of `nums` for each case.

