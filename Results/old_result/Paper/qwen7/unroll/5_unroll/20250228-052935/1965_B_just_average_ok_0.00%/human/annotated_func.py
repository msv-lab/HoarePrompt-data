#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: The number of elements in `nums` list will vary based on the values of `n` and `k` for each test case, but it will always be 3. The elements in `nums` will be [k - (1 << (idx-1)), k + 1, k + (1 << (idx-1)) + 1], where `idx` is the highest index such that \(1 << idx \leq k\). After removing \(1 << idx\), the list will contain these three specific values for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, and k. For each test case, it checks if t is within the range 1 to 1000 and if n and k are within their respective valid ranges. It then constructs a list `nums` containing three specific values based on the value of k and prints the length of this list followed by the list itself. The final state of the program after processing all test cases is that it outputs the number of elements in `nums` (which is always 3) and the elements themselves for each test case.

