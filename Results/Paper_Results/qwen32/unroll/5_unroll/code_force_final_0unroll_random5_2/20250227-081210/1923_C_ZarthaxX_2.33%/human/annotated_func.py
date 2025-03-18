#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each integer c_i is such that 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5, and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: - `ones[i]` will hold the cumulative count of 1s in the `nums` list up to the `i-1` index.
    #   - `sum[i]` will hold the cumulative sum of `nums` list up to the `i-1` index, with each element decreased by 1.
    #
    #Let's formalize this understanding in the output state format:
    #
    #Output State:
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
        
    #State: `ones[i]` will hold the cumulative count of 1s in the `nums` list up to the `i-1` index. `sum[i]` will hold the cumulative sum of `nums` list up to the `i-1` index, with each element decreased by 1.
#Overall this is what the function does:The function processes multiple test cases. Each test case includes an integer `n`, an integer `q`, a list `c` of `n` integers, and `q` queries. Each query is defined by a pair of integers `l_i` and `r_i`. For each query, the function determines if a specific condition is met within the sublist `c[l_i-1:r_i]` and prints 'YES' if the condition is satisfied, otherwise 'NO'.

