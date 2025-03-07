#State of the program right berfore the function call: The function `func_1` is incomplete and does not match the problem description. The correct function definition should be `def func_1(t, n, q, c, queries):` where `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), `n` and `q` are integers representing the length of the array `c` and the number of queries (1 ≤ n, q ≤ 3 · 10^5), `c` is a list of integers where each element is greater than 0 (1 ≤ c_i ≤ 10^9), and `queries` is a list of q tuples, each containing two integers `l_i` and `r_i` (1 ≤ l_i ≤ r_i ≤ n) representing the borders of the i-th subarray. The sum of `n` over all test cases does not exceed 3 · 10^5, and the sum of `q` over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: `ones` is a list where `ones[i]` represents the count of 1s in the `nums` list from index 0 to index `i-1`. `sum` is a list where `sum[i]` represents the cumulative sum of the differences between each element in `nums` from index 0 to index `i-1` and 1.
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
        
    #State: The values of `ones` and `sum` remain unchanged. The loop iterates `q` times, processing input pairs `(l, r)` and printing 'YES' or 'NO' based on the conditions specified in the loop body.
#Overall this is what the function does:The function `func_1` processes a series of queries on an array `nums`. It accepts no parameters directly but reads input from standard input. The input consists of the length of the array `n` and the number of queries `q`, followed by the array `nums` itself. For each query, represented by a pair of integers `(l, r)`, the function determines if the subarray `nums[l-1:r]` can be transformed into a subarray where all elements are 1 by performing a specific operation. The operation involves changing each element to 1 and checking if the total number of changes required is less than or equal to the sum of the differences between each element and 1 in the subarray. The function prints 'YES' if the condition is met for the query, otherwise it prints 'NO'. After processing all queries, the function terminates without returning any value, and the state of the `ones` and `sum` lists remains unchanged.

