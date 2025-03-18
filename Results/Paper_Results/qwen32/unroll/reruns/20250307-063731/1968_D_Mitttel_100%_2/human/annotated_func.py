#State of the program right berfore the function call: a is a list of n integers (1 ≤ a_i ≤ 10^9), p is a list of n integers (1 ≤ p_i ≤ n) representing a permutation, s is a tuple of two integers (P_B, P_S) where 1 ≤ P_B, P_S ≤ n, and k is an integer (1 ≤ k ≤ 10^9).
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
        
    #State: `vis` is updated to mark all visited positions, `mx` holds the maximum value of `cur + k * a[s]`, `cur` holds the cumulative sum of `a[s]` for all visited positions, `k` is 0 if all iterations were used or a positive number if a position was revisited, and `s` is the last visited position.
    return mx
    #The program returns `mx`, which holds the maximum value of `cur + k * a[s]`
#Overall this is what the function does:The function calculates and returns the maximum value of `cur + k * a[s]` by traversing a list `a` using a permutation list `p`, starting from an initial position `s`, and decrementing `k` until all iterations are used or a position is revisited.

