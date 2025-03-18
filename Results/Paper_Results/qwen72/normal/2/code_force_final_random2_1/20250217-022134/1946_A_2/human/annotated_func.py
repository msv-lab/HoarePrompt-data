#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 10^5, representing the length of the array a, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, `t` is an input integer where 1 ≤ t ≤ 10^4, `n` is an input integer where 1 ≤ n ≤ 10^5, `a` is a sorted list of integers input by the user, `p` is `(n + 1) // 2 - 1`, `res` is the count of the element at index `p` in the sorted list `a`. This state is repeated for each of the `t` test cases.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a list `a` of `n` integers. For each test case, the function sorts the list `a`, finds the median element (or the middle element if the list length is odd), counts how many times this median element appears in the list, and prints this count. After processing all test cases, the function completes its execution, leaving no lasting changes to the input variables.

