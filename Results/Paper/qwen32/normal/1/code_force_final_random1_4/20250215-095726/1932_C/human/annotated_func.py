#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^4. s is a string of length n consisting only of the characters 'L' and 'R'. The sum of all n across all test cases does not exceed 2·10^5.
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
        
    #State: `b` contains all elements of `a` in the order specified by `s`, `l` is `n`, and `r` is `-1`.
    ans = []
    p = 1
    for v in reversed(b):
        p = p * v % m
        
        ans.append(p)
        
    #State: `b` contains all elements of `a` in the order specified by `s`, `l` is `n`, `r` is `-1`, `ans` is a list of cumulative products modulo `m` in the order corresponding to the reversed `b`, `p` is the final cumulative product modulo `m`.
    return reversed(ans)
    #The program returns the list `ans` in reverse order, where `ans` is a list of cumulative products modulo `m` in the order corresponding to the reversed `b`.
#Overall this is what the function does:The function `func_1` takes an integer `n`, an integer `m`, a list `a` of `n` integers, and a string `s` of length `n` consisting of 'L' and 'R'. It constructs a new list `b` by selecting elements from `a` based on the directions specified in `s`. Then, it computes a list `ans` of cumulative products of elements in `b` taken modulo `m`, and returns this list in reverse order.

