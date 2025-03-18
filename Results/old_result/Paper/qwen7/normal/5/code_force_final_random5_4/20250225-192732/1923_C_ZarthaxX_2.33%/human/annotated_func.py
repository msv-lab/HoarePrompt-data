#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: `t` is a positive integer, `n` and `q` are positive integers such that 1 ≤ n, q ≤ 3 × 10^5, `c` is a list of n positive integers where 1 ≤ c_i ≤ 10^9, `nums` is a list of integers obtained from input split by spaces, `ones` is a list of length n+1 where each element is 0, `sum` is a list of n+1 elements where each element is 0, `i` is n+1, `ones[n]` is the sum of 1's in `nums` up to index n-1, `sum[n+1]` is the sum of all elements in `nums` minus the count of 1's in `nums`.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be `n+1`. The `ones` list will contain the cumulative count of 1's encountered so far in the `nums` list, with the last element being the total count of 1's in the entire list. The `sum` list will store the cumulative sum of the elements in `nums`, adjusted by subtracting the count of 1's, with the last element being the final adjusted sum.
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
        
    #State: After the loop executes all its iterations, `i` will be `n+1`. The `ones` list will contain the cumulative count of 1's encountered so far in the `nums` list, with the last element being the total count of 1's in the entire list. The `sum` list will store the cumulative sum of the elements in `nums`, adjusted by subtracting the count of 1's, with the last element being the final adjusted sum. Each iteration of the loop processes a query defined by `l` and `r`, and prints 'YES' or 'NO' based on the condition involving `onesInRange` and `sumInRange`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of positive integers and a series of queries. For each query, it checks whether a certain condition involving the count of 1's and the sum of elements in a specified subarray of the list is satisfied. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results of the queries directly.

