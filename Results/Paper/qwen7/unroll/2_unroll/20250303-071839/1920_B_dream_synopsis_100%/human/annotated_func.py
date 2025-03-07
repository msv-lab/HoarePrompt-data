#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are positive integers satisfying 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. The array a consists of n integers where 1 ≤ a_i ≤ 1000 for all i. The sum of n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are positive integers satisfying 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. The array a consists of n integers where 1 ≤ a_i ≤ 1000 for all i. After executing the loop, ans is a list of integers obtained by processing the array a according to the given logic, and the final output is the maximum value in ans. The sum of n across all test cases does not exceed 2⋅10^5.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, k, and x, and an array a of n integers. For each test case, it sorts the array in descending order, calculates a series of sums based on specified conditions involving x and k, and appends these sums to a list. Finally, it prints the maximum value from this list.

