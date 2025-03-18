#State of the program right berfore the function call: a is a list of n integers where each integer is between 1 and 10^9, p is a list of n integers representing a permutation of integers from 1 to n, s is a tuple of two integers (P_B, P_S) where 1 <= P_B, P_S <= n, and k is an integer such that 1 <= k <= 10^9.
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
        
    #State: `a` remains the same, `p` remains the same, `s` is the last state before termination, `k` is `0` if all iterations were used, otherwise the remaining `k`, `mx` is the maximum value of `cur + k * a[s]` encountered, `cur` is the sum of `a[s]` values visited, and `vis` indicates the visited states.
    return mx
    #The program returns mx, which is the maximum value of cur + k * a[s] encountered
#Overall this is what the function does:The function `func_1` accepts a list `a` of `n` integers, a permutation list `p` of integers from 1 to `n`, an integer `s` (initial state), and an integer `k`. It returns the maximum value encountered for the expression `cur + k * a[s]` as it iterates through the list based on the permutation `p`, updating `cur` with the sum of visited `a[s]` values and decrementing `k` until `k` reaches zero or a cycle is detected.

