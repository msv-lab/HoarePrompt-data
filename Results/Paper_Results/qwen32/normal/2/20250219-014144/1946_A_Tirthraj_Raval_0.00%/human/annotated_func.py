#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has executed `t` times. For each iteration, `n` was an input integer, `a` was a sorted list of integers from the input, `p` was calculated as `(n + 1) // 2 - 1`, and `res` was the count of the element at index `p` in `a`. The result `res` for each iteration has been printed.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it sorts the list `a` and prints the count of the median element in the sorted list.

