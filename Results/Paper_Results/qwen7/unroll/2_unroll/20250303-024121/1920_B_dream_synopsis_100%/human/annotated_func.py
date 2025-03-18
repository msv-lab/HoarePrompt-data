#State of the program right berfore the function call: t is a positive integer such that \(1 \leq t \leq 10^4\); for each test case, n, k, and x are positive integers such that \(1 \leq n \leq 2 \cdot 10^5\), \(1 \leq x, k \leq n\); and a list of n integers \(a_1, a_2, \ldots, a_n\) where \(1 \leq a_i \leq 1000\). Additionally, the sum of n over all test cases does not exceed \(2 \cdot 10^5\).
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
        
    #State: Output State: t is a positive integer such that \(1 \leq t \leq 10^4\); for each test case, n, k, and x are positive integers such that \(1 \leq n \leq 2 \cdot 10^5\), \(1 \leq x, k \leq n\); and a list of n integers \(a_1, a_2, \ldots, a_n\) where \(1 \leq a_i \leq 1000\). The output is the maximum value among the sums calculated for each \(i\) from 0 to \(k\) based on the given logic inside the loop, with the sum adjusted according to the elements in the sorted list \(a\).
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, k, x, and a list of n integers a. It sorts the list a in descending order and calculates a series of sums based on specific conditions involving x and k. For each test case, it computes these sums and appends them to a list. Finally, it prints the maximum value among these sums for each test case.

