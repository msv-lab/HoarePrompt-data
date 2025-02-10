#State of the program right berfore the function call: t is a positive integer such that \(1 \leq t \leq 10^4\), each test case consists of n, k, and x where \(1 \leq n \leq 2 \cdot 10^5\), \(1 \leq x, k \leq n\), and an array of n integers \(a_1, a_2, \ldots, a_n\) where \(1 \leq a_i \leq 1000\). The sum of n over all test cases does not exceed \(2 \cdot 10^5\).
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
        
    #State: Output State: After the loop executes all the iterations, the output state will be a list `ans` of length `k + 1`. This list contains the intermediate values of `sums` calculated during each iteration of the loop, starting from the initial value `sum1 - 2 * sum(a[:x + 1])` when `i == 0`. For each subsequent iteration from `i = 1` to `i = k`, the value of `sums` is updated based on the condition `i + x - 1 < n`. If the condition holds, `sums` is updated to `sums + a[i - 1] - 2 * a[i + x - 1]`; otherwise, it is updated to `sums + a[i - 1]`. The final value in the list `ans` corresponds to the maximum value among all the intermediate sums calculated during the loop iterations.
    #
    #In simpler terms, after running the loop for all its iterations, `ans` will hold a list of `k + 1` values, each representing the sum of the array elements under specific conditions, with the last value being the maximum of all these sums.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \(n\), \(k\), and \(x\), along with an array of \(n\) integers. For each test case, it sorts the array in descending order, calculates a series of sums based on specific conditions involving the first \(x+1\) elements and subsequent elements of the array, and stores these sums in a list. Finally, it outputs the maximum value from this list.

