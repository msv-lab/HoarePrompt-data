#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: Output State: `i` is `n`; `sum[n]` is the sum of all elements in `nums`; `ones[n]` is the count of `1`s in `nums`.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be equal to `n`. The `sum[n]` will be the cumulative sum of all elements in the `nums` list. Similarly, `ones[n]` will represent the total count of `1`s present in the `nums` list.
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
        
    #State: After all iterations of the loop, `i` is `0`, `l` and `r` are the last pair of integers entered by the user during the last iteration of the loop, `sumInRange` is `sum[r] - sum[l - 1]`, and `onesInRange` is `ones[r] - ones[l - 1]`. If the condition `2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange` is true, no changes are made. Otherwise, no changes are made.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of positive integers and a set of queries. For each query, it checks whether a specific condition is met based on the count of 1s and the sum of elements within a specified range of the list. If the condition is satisfied, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results of each query.

