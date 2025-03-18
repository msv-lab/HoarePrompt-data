#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: The loop will execute for each test case provided by the user. For each test case, `idx` will be set to the highest power of 2 less than or equal to `k`. After processing all test cases, `nums` will contain the integers from \(2^0\) to \(2^{23}\) (i.e., the powers of 2 up to \(2^{23}\)), along with any additional elements added during the loop execution based on the value of `k` for each test case. Each `nums` list will have its specific `1 << idx` value removed. The final state of `nums` after all iterations will be a combination of these lists, with each list potentially having different additional elements based on the `k` values for each test case. The length of `nums` for each test case will vary depending on the value of `k`, but the overall structure of `nums` will consist of the powers of 2 up to \(2^{23}\) and any additional elements specified by the loop.
    #
    #Since the exact values of `k` for each test case are not specified, we cannot determine the exact contents of `nums` after all iterations. However, we know that `nums` will always include the powers of 2 from \(2^0\) to \(2^{23}\), and may include additional elements based on the `k` values for each test case. The length of `nums` for each test case will be determined by the value of `k` and the operations performed within the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of three values: the number of test cases \(t\), and for each test case, two integers \(n\) and \(k\). For each test case, it calculates and prints the length of a list `nums` which contains the first 24 powers of 2 (from \(2^0\) to \(2^{23}\)) and additional elements based on the value of \(k\). Specifically, it removes one element from this list and appends three new elements. The printed output includes the length of `nums` followed by the elements in `nums`. The final state of `nums` varies for each test case based on the value of \(k\), but it always includes the first 24 powers of 2 and some additional elements.

