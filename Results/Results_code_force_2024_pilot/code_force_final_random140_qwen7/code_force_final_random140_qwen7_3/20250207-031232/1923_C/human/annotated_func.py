#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. The array c is a list of n positive integers where 1 ≤ c_i ≤ 10^9, and for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `nums` is a list of integers obtained from the input split by spaces, `ones` is a list of n+1 integers initialized to zero, `sum` is a list of n+1 integers initialized to zero, `i` is n+1, `sum[n]` is `sum[n-1] + nums[n-1]`, `ones[n-1]` is `ones[n-2] + (1 if nums[n-2] == 1 else 0)`.
    #
    #This means after the loop has executed all its iterations, the variable `i` will be equal to `n+1`. The `sum` list will have its last element as the sum of all elements in the `nums` list, since it accumulates the sum of `nums[i-1]` at each iteration. Similarly, the `ones` list will have its last element as the count of `1`s in the `nums` list up to the last index, since it increments by 1 whenever `nums[i-1]` is `1`.
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
        
    #State: `t` is a positive integer, `n` is an input integer, `q` is 0, `nums` is a list of integers obtained from the input split by spaces, `ones` is a list of n+1 integers initialized to zero, `sum` is a list of n+1 integers initialized to zero, `i` is n+1, `sum[n]` is `sum[n-1] + nums[n-1]`, `ones[n-1]` is `ones[n-2] + (1 if nums[n-2] == 1 else 0)`, `l` and `r` are undefined, `sumInRange` and `onesInRange` are undefined.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the number of elements `n` and the number of queries `q`. It then reads an array `nums` of `n` positive integers. For each query, it reads the range `l` and `r` and checks if the condition `2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange` is satisfied. If the condition holds, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results of the queries.

