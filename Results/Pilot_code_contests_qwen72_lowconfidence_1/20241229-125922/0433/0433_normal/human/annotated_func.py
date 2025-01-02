#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000, and A is a list of n integers where each element ai satisfies 0 ≤ ai ≤ 109.
def func():
    n = input()
    a = [input() for i in xrange(n)]
    dp = [float('inf') for _ in xrange(n)]
    for i in xrange(n):
        dp[bisect.bisect_left(dp, a[i])] = a[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer, `A` is a list of `n` integers where each element `ai` satisfies \(0 \leq ai \leq 10^9\), `a` is a list of `n` strings where each element is an input string, `dp` is a list of `n` elements where each element is a value from `a` in non-decreasing order. If `n` is 0, `dp` is an empty list.
    for i in xrange(n):
        if dp[i] == float('inf'):
            print(i)
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer, `A` is a list of `n` integers where each element `ai` satisfies \(0 \leq ai \leq 10^9\), `a` is a list of `n` strings where each element is an input string, `dp` is a list of `n` elements where each element is a value from `a` in non-decreasing order. If `n` is 0, `dp` is an empty list and no value is printed. If `n` is greater than 0, `i` will be the index of the first `float('inf')` in `dp` if it exists, and this value will be printed. If no `float('inf')` is found, `i` will be `n-1` and no value will be printed.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers `a` from user input. It then processes these inputs to find the length of the longest increasing subsequence (LIS) of `a`. The function constructs a dynamic programming array `dp` where each element represents the smallest possible last element of an increasing subsequence of a given length. After processing, the function prints the length of the LIS. If the input list `a` is empty (`n` is 0), the function prints 0. If the input list `a` contains elements, the function prints the length of the LIS.

