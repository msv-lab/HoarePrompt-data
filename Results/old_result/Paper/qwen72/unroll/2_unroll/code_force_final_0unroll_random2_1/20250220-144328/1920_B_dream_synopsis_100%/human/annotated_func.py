#State of the program right berfore the function call: t is an integer such that 1 \leq t \leq 10^4, n, k, and x are integers for each test case such that 1 \leq n \leq 2 \cdot 10^5, 1 \leq k, x \leq n, and a_1, a_2, \ldots, a_n are integers such that 1 \leq a_i \leq 1000. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: The loop has finished executing, and the maximum value from the list `ans` has been printed for each test case. The variables `t`, `n`, `k`, `x`, and `a` retain their values as they were at the end of the last iteration of the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads three integers `n`, `k`, and `x`, followed by a list of `n` integers. It then processes these inputs to compute a series of values, ultimately printing the maximum value from this series for each test case. The function does not return any value. After the function concludes, the variables `t`, `n`, `k`, `x`, and `a` retain their values as they were at the end of the last iteration of the loop.

