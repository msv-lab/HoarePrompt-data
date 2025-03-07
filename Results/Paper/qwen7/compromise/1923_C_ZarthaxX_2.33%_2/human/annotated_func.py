#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `nums` is a list of integers obtained from the input split by spaces, `ones` is a list of n+1 integers where each element starting from index 1 is the cumulative count of 1s up to that index in `nums`, `sum` is a list of n+1 integers where each element starting from index 1 is the cumulative sum of `nums` up to that index minus the index value.
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
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `nums` is a list of integers obtained from the input split by spaces, `ones` is a list of n+1 integers where each element starting from index 1 is the cumulative count of 1s up to that index in `nums`, `sum` is a list of n+1 integers where each element starting from index 1 is the cumulative sum of `nums` up to that index minus the index value, `q` is decremented after each iteration of the loop, `l` and `r` are updated with values read from input for each iteration of the loop, `onesInRange` and `sumInRange` are recalculated for each iteration based on the current values of `l` and `r`. The loop prints 'YES' or 'NO' based on the condition given for each pair of `l` and `r`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \( n \) and \( q \), a list \( c \) of \( n \) positive integers, and \( q \) queries. Each query includes two positive integers \( l_i \) and \( r_i \). For each query, the function calculates whether the sum of elements in the subarray from index \( l_i \) to \( r_i \) can be made non-negative by flipping at most one 0 to 1 in the subarray. If such a flip can achieve a non-negative sum, the function prints 'YES'; otherwise, it prints 'NO'. After processing all queries, the function concludes without returning any value.

