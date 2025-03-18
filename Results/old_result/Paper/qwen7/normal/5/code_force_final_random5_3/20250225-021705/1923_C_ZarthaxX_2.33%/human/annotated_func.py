#State of the program right berfore the function call: t is a positive integer, each test case contains n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q queries defined by pairs of integers l_i and r_i representing the subarray boundaries.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: `ones` is a list of length `n + 1` where the first element is 1 and the rest are 0, `sum` is a list of length `n + 1` where each element is the cumulative sum of `nums` minus 1 up to that index.
    #
    #To explain this output state in natural language:
    #After the loop has executed all its iterations, the variable `ones` will still have its first element as 1 and all other elements as 0. This is because the loop updates only `ones[i]` to `ones[i - 1] + 1` if `nums[i - 1]` is 1, but it does not change any other elements in `ones`. The variable `sum` will contain the cumulative sum of the elements in `nums` minus 1 up to each index. This means that `sum[i]` will be the sum of `nums[0] - 1, nums[1] - 1, ..., nums[i-1] - 1`. All other variables (`n`, `q`, `t`, `c`, `nums`) remain unchanged as they are not modified within the loop.
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
        
    #State: `ones` is a list of length `n + 1` where the first element is 1 and the rest are 0, `sum` is a list of length `n + 1` where each element is the cumulative sum of `nums` minus 1 up to that index, `q` is `q - 3`, `l` and `r` are updated to their final values obtained from the last input, and `onesInRange` is `ones[r] - ones[l - 1]`, `sumInRange` is `sum[r] - sum[l - 1]`.
#Overall this is what the function does:The function processes a series of queries on a given array. It calculates and prints 'YES' or 'NO' based on whether the sum of elements in a specified subarray meets a certain condition involving the count of 1s in that subarray. Specifically, for each query defined by indices \( l \) and \( r \), it checks if \( 2 \times \text{count of 1s in } [l, r] + (r - l + 1) - \text{count of 1s in } [l, r] \leq \text{sum of elements in } [l, r] \). If true, it prints 'YES'; otherwise, 'NO'. The function does not return any value but modifies global variables `ones` and `sum` during its execution.

