#State of the program right berfore the function call: a is a list of n integers where each integer is between 1 and 10^9 inclusive, p is a list of n integers representing a permutation of integers from 1 to n, s is a list of 4 integers where s[0] is the number of test cases t, s[1] is the length of the permutation n, s[2] is Bodya's starting position P_B, s[3] is Sasha's starting position P_S, n is between 1 and 2 * 10^5 inclusive, k is a non-negative integer between 1 and 10^9 inclusive, and the sum of all n over all test cases does not exceed 2 * 10^5.
def func_1(a, p, s, k):
    n = len(p)
    mx = 0
    cur = 0
    vis = [(0) for _ in range(n)]
    while not vis[s] and k > 0:
        vis[s] = 1
        
        mx = max(mx, cur + k * a[s])
        
        cur += a[s]
        
        k -= 1
        
        s = p[s]
        
    #State: mx, cur, k, vis, s.
    return mx
    #The program returns the value of `mx`.
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers, a permutation list `p`, a list `s` containing test case parameters, and an integer `k`. It returns the maximum value `mx` calculated based on the values in `a`, the permutation in `p`, the starting position indicated by `s`, and the decrementing value `k`.

