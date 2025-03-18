#State of the program right berfore the function call: t is a positive integer, each test case contains two integers n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q queries defined by pairs of integers l_i and r_i where 1 <= l_i <= r_i <= n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: Output State: `i` is `n`; `ones[n]` is the sum of all elements in `nums` where the value is 1; `sum[n]` is the sum of all elements in `nums`.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` will be equal to `n`. The `ones` list will contain the cumulative count of the number 1s up to each index, and the `sum` list will contain the cumulative sum of the elements in `nums` up to each index.
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
        
    #State: Output State: `i` is `n`, `ones[n]` is the sum of all elements in `nums` where the value is 1, `sum[n]` is the sum of all elements in `nums`, `q` is `0`, and `l` and `r` are the last values entered by the user during the loop's final iteration. The `onesInRange` and `sumInRange` variables are calculated based on these final `l` and `r` values but do not affect the overall state since the loop has completed.
    #
    #Explanation: After all iterations of the loop have finished, the variable `i` will be equal to `n`. The `ones` list will contain the cumulative count of the number 1s up to each index, and the `sum` list will contain the cumulative sum of the elements in `nums` up to each index. The variable `q` will be `0` because it starts with a positive value and is decremented by `1` in each iteration until it reaches `0`. The variables `l` and `r` will hold the values from the last input pair processed by the loop. The `onesInRange` and `sumInRange` calculations are performed using these final `l` and `r` values but do not change the overall state since the loop has ended.
#Overall this is what the function does:The function processes a series of queries on a given array. It first constructs cumulative counts and sums for the array elements. Then, for each query, it checks if a specific condition is met based on the subarray defined by the query indices. If the condition is satisfied, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results of the queries.

