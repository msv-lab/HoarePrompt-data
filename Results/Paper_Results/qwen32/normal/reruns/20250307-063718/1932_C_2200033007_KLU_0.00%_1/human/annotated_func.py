#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, for each test case, n is an integer such that 1 <= n <= 2*10^5, m is an integer such that 1 <= m <= 10^4, a is a list of integers of length n where each element a_i satisfies 1 <= a_i <= 10^4, and s is a string of length n consisting of characters 'L' and 'R'. The sum of all n across all test cases does not exceed 2*10^5.
def func_1(n, m, a, s):
    b = []
    l = 0
    r = n - 1
    for i in range(n):
        if s[i] == 'L':
            b.append(a[l])
            l += 1
        else:
            b.append(a[r])
            r -= 1
        
    #State: `b` contains `n` elements chosen from `a` according to `s`, `l` is `n`, and `r` is `-1`.
    ans = []
    p = 1
    for v in reversed(b):
        p = p * v
        
        ans.append(p)
        
    #State: `b` contains `n` elements chosen from `a` according to `s`; `l` is `n`; `r` is `-1`; `ans` is `[b[n-1], b[n-1] * b[n-2], ..., b[n-1] * b[n-2] * ... * b[1], b[n-1] * b[n-2] * ... * b[0]]`; `p` is `b[n-1] * b[n-2] * ... * b[0]`.
    return reversed(ans)
    #The program returns a reversed list `ans` where `ans` is `[b[n-1], b[n-1] * b[n-2], ..., b[n-1] * b[n-2] * ... * b[1], b[n-1] * b[n-2] * ... * b[0]]`. The reversed list will be `[b[n-1] * b[n-2] * ... * b[0], b[n-1] * b[n-2] * ... * b[1], ..., b[n-1] * b[n-2], b[n-1]]`.
#Overall this is what the function does:The function `func_1` takes four parameters: `n` (an integer), `m` (an integer, though not used in the function), `a` (a list of integers of length `n`), and `s` (a string of length `n` consisting of characters 'L' and 'R'). It constructs a list `b` by selecting elements from `a` based on the characters in `s` ('L' selects from the left, 'R' from the right). Then, it computes a list `ans` where each element is the cumulative product of elements from `b` in reverse order, starting from the last element to the first. The function returns this list `ans` in reverse order.

