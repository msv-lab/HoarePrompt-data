#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. The array c is a list of n positive integers where each element is between 1 and 10^9 inclusive. Each query is defined by two integers l_i and r_i such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `nums` is a list of integers obtained from the input split by spaces, `ones` is a list of n+1 elements where each element is calculated as the cumulative count of 1s up to that index in `nums`, `sum` is a list of n+1 elements where each element is calculated as the cumulative sum of `nums` up to that index minus the index value.
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
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `nums` is a list of integers obtained from the input split by spaces, `ones` is a list of n+1 elements where each element is calculated as the cumulative count of 1s up to that index in `nums`, `sum` is a list of n+1 elements where each element is calculated as the cumulative sum of `nums` up to that index minus the index value, `q` is decremented after each iteration of the loop until it reaches 0, `l` and `r` are updated with values provided by user input for each iteration of the loop, `onesInRange` and `sumInRange` are recalculated based on the current values of `l` and `r` for each iteration, and the loop prints either 'YES' or 'NO' based on the condition for each iteration. After all iterations, `q` will be 0.
#Overall this is what the function does:The function processes a series of queries on an array of integers. It first calculates the cumulative count of 1s and the modified cumulative sum (each element reduced by its index) up to each position in the array. For each query, it checks if a certain condition is met within the specified range of the array and prints 'YES' or 'NO' accordingly. After processing all queries, the function concludes.

