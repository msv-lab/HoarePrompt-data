#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: The output state will consist of multiple lines, each representing the result of one test case. For each test case, two lines will be printed: the first line contains the length of the list `nums` after modifications, and the second line contains the elements of the list `nums` in ascending order. The list `nums` will always contain unique elements and will have a maximum length of 23 (since it starts with 21 elements and can add up to 2 more). The elements in `nums` will be powers of 2, adjusted by the value of `k`, and will include `k-nums[idx]`, `k+1`, and `k+nums[idx]+1`, where `idx` is the index just before the first element in `nums` that is greater than `k`.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers \( n \) and \( k \). It constructs a list `nums` containing specific values derived from \( k \) and prints the length and contents of this list for each test case. The list `nums` includes powers of 2, adjusted by \( k \), and additional values \( k - \text{nums}[i] \), \( k + 1 \), and \( k + \text{nums}[i] + 1 \), where \( \text{nums}[i] \) is the largest power of 2 less than or equal to \( k \). The final state of the program after each test case is the output of the length and sorted list `nums`.

