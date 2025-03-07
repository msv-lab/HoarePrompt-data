#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element is greater than 0 and 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5 and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 3 * 10^5; `q` is an integer such that 1 <= q <= 3 * 10^5; `c` is a list of `n` integers where each element is greater than 0 and 1 <= c_i <= 10^9; `nums` is a list of integers derived from the input; `ones` is a list of `n + 1` integers where `ones[i]` is the count of 1s in the first `i-1` elements of `nums`; `sum` is a list of `n + 1` integers where `sum[i]` is the sum of the first `i-1` elements of `nums` minus `i-1`; `i` is `n`.
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
        
    #State: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 3 * 10^5, q is 0, c is a list of n integers where each element is greater than 0 and 1 <= c_i <= 10^9, nums is a list of integers derived from the input, ones is a list of n + 1 integers where ones[i] is the count of 1s in the first i-1 elements of nums, sum is a list of n + 1 integers where sum[i] is the sum of the first i-1 elements of nums minus i-1, i is n.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an integer `n`, an integer `q`, and a list of `n` integers. It then processes `q` queries, each defined by two integers `l_i` and `r_i`. For each query, it checks if a specific condition is met on the sublist of integers from index `l_i` to `r_i` (inclusive) and prints 'YES' if the condition is satisfied, otherwise 'NO'.

