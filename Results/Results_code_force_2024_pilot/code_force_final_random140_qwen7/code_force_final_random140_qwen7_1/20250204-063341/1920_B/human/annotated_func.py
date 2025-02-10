#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n; and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 1000. Additionally, the sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
                sums = sum1 - 2 * sum(a[:x + 1])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: Output State: After the loop executes all iterations, the variable `i` will be equal to `k + 1`. The variable `sums` will hold the final value after all updates based on the conditions provided in the loop. The list `ans` will contain `k + 1` elements, each representing the value of `sums` after each iteration of the loop from `i = 0` to `i = k`. The maximum value among these elements will be printed as the final output.
    #
    #In natural language, this means that after the loop completes all its iterations, the list `ans` will store all intermediate results of the variable `sums` calculated for each value of `i` from 0 to `k`. The final output will be the maximum value found in this list `ans`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), \( k \), \( x \), and a list of integers \( a \). For each test case, it sorts the list \( a \) in descending order, calculates a series of sums based on specific conditions involving \( k \), \( x \), and the elements of \( a \), stores these sums in a list, and finally prints the maximum value from this list.

