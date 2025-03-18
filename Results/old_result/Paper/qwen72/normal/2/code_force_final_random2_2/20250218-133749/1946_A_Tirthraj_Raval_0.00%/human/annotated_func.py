#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, representing the length of the array a. The array a consists of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, all test cases have been processed, and for each test case, `n` was an input integer, `a` was a sorted list of integers provided by the user, `p` was calculated as `(n + 1) // 2 - 1`, and `res` was the count of the element at index `p` in the list `a`.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. It sorts the list `a`, calculates the count of the median element in the sorted list, and prints this count. After processing all test cases, the function completes, and no value is returned. The state of the program is such that all test cases have been processed, and the counts of the median elements for each test case have been printed.

