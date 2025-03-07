#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ x, k ≤ n, and a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it prints the maximum value from the list `ans` which contains the calculated sums after applying the specified operations. The variables `t`, `n`, `k`, `x`, and `a` are updated and used in each iteration, but their final values after the loop are not relevant to the output. The output state is the sequence of maximum values printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, `x`, and a list `a` of integers. For each test case, it calculates a series of sums based on the elements of `a` and the values of `k` and `x`. It then prints the maximum value from these calculated sums. The function does not return any value; instead, it outputs the maximum sum for each test case. After the function concludes, the sequence of maximum values for each test case is printed, and the internal variables used for calculations are reset for the next test case.

