#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. For each test case, n is a positive integer (1 ≤ n ≤ 10^5), representing the length of the array a, and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an input integer between 1 and 10^4, `_` is `t-1`, `n` is a new input integer, `a` is a sorted list of integers input by the user, `p` is `(n + 1) // 2 - 1`, `res` is the number of times the element at index `p` appears in the list `a`.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case involves an integer `n` and a list of `n` integers `a`. For each test case, it sorts the list `a`, finds the median element (or the middle element if `n` is odd), and prints the count of how many times this median element appears in the list. After processing all test cases, the function has printed the count for each test case. The function does not return any value; it only prints the results.

