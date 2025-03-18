#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5. c is a list of n integers where each integer c_i satisfies 1 ≤ c_i ≤ 10^9. There are q queries, and for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: `ones` is a list of `n + 1` integers where `ones[i]` represents the count of `1`s in the `nums` list from index `0` to `i-1`. `sum` is a list of `n + 1` integers where `sum[i]` represents the sum of all elements in the `nums` list from index `0` to `i-1`, minus the number of elements in that range.
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
        
    #State: `ones` is a list of `n + 1` integers where `ones[i]` represents the count of `1`s in the `nums` list from index `0` to `i-1`. `sum` is a list of `n + 1` integers where `sum[i]` represents the sum of all elements in the `nums` list from index `0` to `i-1`, minus the number of elements in that range.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines if a specific condition is met within a sublist of the list and prints 'YES' or 'NO' accordingly.

