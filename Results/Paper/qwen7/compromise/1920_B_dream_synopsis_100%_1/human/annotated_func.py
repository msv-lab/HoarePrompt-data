#State of the program right berfore the function call: t is a positive integer such that \(1 \leq t \leq 10^4\); for each test case, n, k, and x are positive integers such that \(1 \leq n \leq 2 \cdot 10^5\), \(1 \leq k, x \leq n\); and a list of n integers \(a_1, a_2, \ldots, a_n\) where \(1 \leq a_i \leq 1000\) for all \(i\). The sum of n over all test cases does not exceed \(2 \cdot 10^5\).
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
        
    #State: Output State: The loop will execute exactly `k + 1` times. After all iterations, the variable `i` will be equal to `k`, `k` remains a non-negative integer, `sums` will be updated based on the conditions within the loop, and `ans` will contain `k + 1` elements, each being the value of `sums` after each iteration of the loop. The final value of `ans` will be a list of length `k + 1`, where each element represents the maximum sum calculated after considering different segments of the sorted list `a` under the given conditions. The final element of `ans` will be the maximum value among all the sums calculated during the iterations, which is printed by the code.
    #
    #In more detail, after the loop completes:
    #- `i` will be `k`.
    #- `k` remains unchanged.
    #- `sums` will hold the final value after the last iteration.
    #- `ans` will be a list of `k + 1` elements, where each element is the value of `sums` after each iteration from `i = 0` to `i = k`. The final output printed is the maximum value in this list `ans`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it sorts a list of integers in descending order and then calculates the sum of different segments of this list. Specifically, it computes the sum of the entire list minus twice the sum of the first x elements, and for each subsequent segment of length k, it adjusts the sum by adding the previous element and subtracting twice the next element in the sorted list. The function outputs the maximum sum obtained from these calculations for each test case.

