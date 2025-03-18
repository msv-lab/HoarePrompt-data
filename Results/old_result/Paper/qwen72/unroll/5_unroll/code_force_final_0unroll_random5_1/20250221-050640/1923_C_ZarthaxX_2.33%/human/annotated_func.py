#State of the program right berfore the function call: The function `func_1` is intended to process multiple test cases, where each test case includes an array `c` of positive integers and a set of queries `q`. The array `c` has a length `n` (1 ≤ n ≤ 3 · 10^5), and each element `c_i` is a positive integer (1 ≤ c_i ≤ 10^9). The number of queries `q` is also a positive integer (1 ≤ q ≤ 3 · 10^5). Each query consists of two integers `l_i` and `r_i` (1 ≤ l_i ≤ r_i ≤ n) representing the start and end indices of a subarray of `c`. The sum of `n` over all test cases does not exceed 3 · 10^5, and the sum of `q` over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: `ones` is a list where each element at index `i` represents the count of 1s in the `nums` list from index 0 to `i-1`. `sum` is a list where each element at index `i` represents the cumulative sum of the differences between each element in `nums` from index 0 to `i-1` and 1.
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
        
    #State: The values of `ones` and `sum` remain unchanged, and the loop has printed 'YES' or 'NO' for each iteration based on the conditions specified in the loop.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an array `c` of positive integers and a set of queries `q`. It reads the length of the array `n` and the number of queries `q` from input, followed by the array `c`. The function then computes two auxiliary arrays: `ones`, which tracks the cumulative count of 1s in `c` up to each index, and `sum`, which tracks the cumulative sum of the differences between each element in `c` and 1. For each query, defined by indices `l_i` and `r_i`, the function checks a specific condition involving the count of 1s and the sum of differences within the subarray from `l_i` to `r_i`. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value, and the auxiliary arrays `ones` and `sum` remain unchanged after the function concludes.

