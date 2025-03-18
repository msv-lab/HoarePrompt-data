#State of the program right berfore the function call: t is a positive integer, each test case consists of two integers n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q subarray queries defined by pairs of integers l_i and r_i where 1 <= l_i <= r_i <= n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: `t` is a positive integer, `n` is the length of the array `nums`, `q` is an input integer representing the number of subarray queries, `nums` is a list of integers created by splitting the input string on spaces and converting each element to an integer, `ones` is a list of n+1 integers where each element represents the cumulative count of 1s up to that index in `nums`, `sum` is a list of n+1 integers where each element represents the cumulative sum of elements in `nums` up to that index minus the index itself.
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
        
    #State: Output State: `t` is a positive integer, `n` is the length of the array `nums`, `q` is an input integer representing the number of subarray queries, `nums` is a list of integers created by splitting the input string on spaces and converting each element to an integer, `ones` is a list of n+1 integers where each element represents the cumulative count of 1s up to that index in `nums`, `sum` is a list of n+1 integers where each element represents the cumulative sum of elements in `nums` up to that index minus the index itself, after executing all the iterations of the loop, for each query `(l, r)`, a 'YES' or 'NO' has been printed based on the condition `2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange`.
#Overall this is what the function does:The function processes a set of inputs including a positive integer `t`, an array `nums` of length `n` where each element is a positive integer not exceeding 10^9, and `q` subarray queries defined by pairs of integers `l_i` and `r_i` where 1 <= `l_i` <= `r_i` <= `n`. For each query, it checks whether the condition `2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange` holds true, where `onesInRange` is the count of 1s in the subarray from index `l` to `r`, and `sumInRange` is the sum of elements in the subarray from index `l` to `r` minus the index values. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all queries, the function does not return any value but prints 'YES' or 'NO' for each query.

