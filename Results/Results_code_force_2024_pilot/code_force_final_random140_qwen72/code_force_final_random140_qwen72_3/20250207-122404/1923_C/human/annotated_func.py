#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; for each of the q queries, l_i and r_i are integers where 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: After the loop executes all iterations, `t` remains an integer where 1 ≤ t ≤ 10^4, `n` remains an input integer where 1 ≤ n ≤ 3 · 10^5, `q` remains an input integer where 1 ≤ q ≤ 3 · 10^5, `c` remains a list of n integers where 1 ≤ c_i ≤ 10^9, `nums` remains a list of integers obtained from the input, `ones` is a list of length n + 1 where `ones[i]` is the cumulative count of 1s in `nums` up to index `i-1`, `sum` is a list of length n + 1 where `sum[i]` is the cumulative sum of elements in `nums` up to index `i-1`, `i` is `n`, and `n` must be greater than or equal to 1.
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
        
    #State: After the loop executes all iterations, `t` remains an integer where 1 ≤ t ≤ 10^4, `n` remains an input integer where 1 ≤ n ≤ 3 · 10^5, `q` remains an input integer where 1 ≤ q ≤ 3 · 10^5, `c` remains a list of n integers where 1 ≤ c_i ≤ 10^9, `nums` remains a list of integers obtained from the input, `ones` remains a list of length n + 1 where `ones[i]` is the cumulative count of 1s in `nums` up to index `i-1`, `sum` remains a list of length n + 1 where `sum[i]` is the cumulative sum of elements in `nums` up to index `i-1`, `i` remains `n`, `n` must be greater than or equal to 1, and `q` must be greater than or equal to 0. The loop has executed `q` times, and for each iteration, the values of `l` and `r` were taken from user input, and the conditions within the loop were checked and printed accordingly.
#Overall this is what the function does:The function `func_1` processes a series of test cases. For each test case, it reads the length of a list `n` and the number of queries `q`. It then reads a list of integers `nums` of length `n`. The function calculates two auxiliary lists: `ones`, which stores the cumulative count of 1s in `nums` up to each index, and `sum`, which stores the cumulative sum of elements in `nums` up to each index. For each of the `q` queries, it reads a range `[l, r]` and checks if the condition \(2 \times \text{onesInRange} + (r - l + 1) - \text{onesInRange} \leq \text{sumInRange}\) holds, where `onesInRange` and `sumInRange` are the counts of 1s and the sum of elements in the range `[l, r]` respectively. If the condition is true, it prints 'YES'; otherwise, it prints 'NO'. After processing all queries, the function completes without returning any value.

