#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, representing the length of the array a. The array a consists of n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 · 10^5.
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: After all iterations, `t` is an input integer such that 1 ≤ t ≤ 10^4, `n` is the last input integer, `a` is a sorted list of integers input by the user, `p` is `(n + 1) // 2 - 1`, `res` is the number of times the element at index `p` appears in the sublist `a[p:]`. The loop has executed `t` times, and for each test case, the result `res` has been printed.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by an array `a` of `n` integers. For each test case, the function sorts the array `a`, finds the median element (or the first median element if the array length is even), and counts how many times this median element appears in the second half of the sorted array. The function prints this count for each test case. After processing all test cases, the function terminates.

