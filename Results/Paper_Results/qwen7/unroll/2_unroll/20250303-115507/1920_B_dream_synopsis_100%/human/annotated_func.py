#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. a is a list of n integers where 1 ≤ a_i ≤ 1000 for all i. The sum of n across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: Output State: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. a is a list of n integers where 1 ≤ a_i ≤ 1000 for all i. After executing the loop, the variable ans contains a list of maximum sums calculated based on the conditions provided in the loop. The final output prints the maximum value from the ans list for each test case.
#Overall this is what the function does:The function accepts a positive integer `t` representing the number of test cases. For each test case, it takes integers `n`, `k`, and `x`, and a list `a` of `n` integers. It sorts the list `a` in descending order, calculates a series of sums based on specified conditions involving `k` and `x`, stores these sums in a list `ans`, and finally prints the maximum value from `ans` for each test case.

