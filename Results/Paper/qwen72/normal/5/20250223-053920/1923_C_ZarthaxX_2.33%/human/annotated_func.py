#State of the program right berfore the function call: The function `func_1` is incomplete and does not match the problem description. The correct function definition should include parameters for the array `c`, the number of queries `q`, and the queries themselves. The correct function definition should be `def func_1(t, n, q, c, queries):` where `t` is the number of test cases (1 ≤ t ≤ 10^4), `n` is the length of the array `c` (1 ≤ n ≤ 3 · 10^5), `q` is the number of queries (1 ≤ q ≤ 3 · 10^5), `c` is a list of positive integers (1 ≤ c_i ≤ 10^9), and `queries` is a list of tuples, each containing two integers `l_i` and `r_i` (1 ≤ l_i ≤ r_i ≤ n) representing the borders of the subarray for each query.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: `ones` is a list where `ones[i]` contains the count of 1s in the sublist `nums[0:i]` for each `i` from 1 to `n`. `sum` is a list where `sum[i]` contains the cumulative sum of the differences between each element in the sublist `nums[0:i]` and 1 for each `i` from 1 to `n`. The values of `nums`, `n`, `q`, `t`, `c`, and `queries` remain unchanged.
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
        
    #State: The values of `ones` and `sum` remain unchanged. The values of `nums`, `n`, `q`, `t`, `c`, and `queries` also remain unchanged. The loop has processed `q` queries, and for each query, it has printed 'YES' or 'NO' based on the conditions specified in the loop body.
#Overall this is what the function does:The function `func_1` processes a series of queries on an array `nums`. It accepts no parameters and reads input from the standard input. The function initializes two lists, `ones` and `sum`, to keep track of the cumulative count of 1s and the cumulative sum of differences from 1, respectively, for the elements in `nums`. For each query, it determines if the condition `2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange` is satisfied for the subarray from index `l` to `r` (inclusive). If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value and does not modify the input array `nums` or any other external variables.

