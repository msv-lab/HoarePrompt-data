#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers where 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: After the loop has executed all iterations:
    for _ in range(q):
        l, r = map(int, input().split(' '))
        
        if l == r:
            print('NO')
            continue
        
        onesInRange = ones[r] - ones[l - 1]
        
        sumInRange = sum[r] - sum[l - 1]
        
        if 2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange:
            print('YES')
        else:
            print('NO')
        
    #State: After the loop executes all iterations, `q` is greater than or equal to 0, `_` is `q-1`, `l` and `r` are the last set of input integers, `onesInRange` is `ones[r] - ones[l - 1]`, and `sumInRange` is `sum[r] - sum[l - 1]`. If `l` is equal to `r`, the loop would have printed 'NO' and continued to the next iteration. If `l` is not equal to `r`, the loop would have evaluated the condition `2 * onesInRange + (r - l + 1) - onesInRange` and printed 'YES' if it is less than or equal to `sumInRange`, otherwise it would have printed 'NO'. The loop has completed all `q` iterations.
#Overall this is what the function does:The function `func_1` reads input values for multiple test cases, each consisting of an integer `n` and an integer `q`. It then reads a list of `n` integers. For each of the `q` queries, it reads two integers `l` and `r`, representing a segment of the list from index `l` to `r`. The function calculates the number of ones and the sum of elements within the specified segment. It prints 'YES' if twice the number of ones plus the length of the segment minus the number of ones is less than or equal to the sum of the segment; otherwise, it prints 'NO'. After processing all queries, the function completes, and the state of the program reflects the completion of all input queries.

