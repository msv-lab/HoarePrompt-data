#State of the program right berfore the function call: The function `func_1` is incomplete and does not match the problem description. The correct function definition should include parameters for the array `c`, the number of queries `q`, and the queries themselves. The precondition for the function should be: `c` is a list of positive integers with length `n` (1 ≤ n ≤ 3 · 10^5), `q` is a non-negative integer (1 ≤ q ≤ 3 · 10^5) representing the number of queries, and each query is a tuple `(l, r)` where `1 ≤ l ≤ r ≤ n`. The sum of `n` over all test cases and the sum of `q` over all test cases do not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: `n` is a positive integer (1 ≤ n ≤ 3 · 10^5), `q` is a non-negative integer (1 ≤ q ≤ 3 · 10^5), `c` is a list of positive integers with length `n`, `nums` is a list of integers with length `n`, `ones` is a list of integers with length `n + 1` where `ones[i]` is the cumulative count of 1s in `nums` up to index `i - 1`, `sum` is a list of integers with length `n + 1` where `sum[i]` is the cumulative sum of `nums[j] - 1` for all `j` from 0 to `i - 1`.
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
        
    #State: `n` is a positive integer (1 ≤ n ≤ 3 · 10^5), `q` is a non-negative integer (1 ≤ q ≤ 3 · 10^5) and must be 0, `c` is a list of positive integers with length `n`, `nums` is a list of integers with length `n`, `ones` is a list of integers with length `n + 1` where `ones[i]` is the cumulative count of 1s in `nums` up to index `i - 1`, `sum` is a list of integers with length `n + 1` where `sum[i]` is the cumulative sum of `nums[j] - 1` for all `j` from 0 to `i - 1`.
#Overall this is what the function does:The function `func_1` processes a series of queries on a list of positive integers. It reads the length of the list `n` and the number of queries `q` from the input. It then reads the list of integers `nums` from the input. For each query `(l, r)`, it determines if the condition `2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange` is met, where `onesInRange` is the count of 1s in the subarray `nums[l-1:r]` and `sumInRange` is the sum of `nums[j] - 1` for all `j` in the range `[l-1, r-1]`. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all queries, the function does not return any value, but the state of the program includes the original list `nums`, the cumulative count of 1s in `nums` (`ones`), and the cumulative sum of `nums[j] - 1` (`sum`).

