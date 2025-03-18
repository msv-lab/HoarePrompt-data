#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: The output state after the loop executes all its iterations will include `i` being 21, `idx` being 19, and `nums` being a list containing all powers of 2 from \(2\) up to \(1048576\), plus \(k-1048576\), \(k+1\), and \(k+1048576+1\), with the element \(1048576\) removed. The exact content of `nums` depends on the value of `k`, but it will always include the numbers \(2, 4, 8, \ldots, 1048576, k-1048576, k+1, k+1048576+1\), excluding \(1048576\).
    #
    #In simpler terms, after all iterations, `nums` will contain all powers of 2 from \(2\) to \(1048576\) inclusive, along with three additional numbers derived from `k`: \(k-1048576\), \(k+1\), and \(k+1048576+1\), with the number \(1048576\) removed from the list.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \(n\) and \(k\). It then constructs a list `nums` containing all powers of 2 from \(2\) to \(1048576\) inclusive, along with three additional numbers derived from \(k\): \(k-1048576\), \(k+1\), and \(k+1048576+1\), with the number \(1048576\) removed from the list. Finally, it prints the length of the list `nums` followed by the elements of `nums`.

