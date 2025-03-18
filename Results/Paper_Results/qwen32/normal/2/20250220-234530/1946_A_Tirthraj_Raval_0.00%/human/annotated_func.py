#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n is a positive integer such that 1 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: `t` is an input integer such that 0 <= `t` <= 10^4, `n` is the last input integer, `a` is the last input list of integers sorted in non-decreasing order, `p` is `(n + 1) // 2 - 1` using the last `n`, `res` is the count of `a[p]` in the sorted list `a` using the last `n`.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of a list of integers. For each test case, it sorts the list and then determines the frequency of the median value in the sorted list, printing this frequency as the result.

