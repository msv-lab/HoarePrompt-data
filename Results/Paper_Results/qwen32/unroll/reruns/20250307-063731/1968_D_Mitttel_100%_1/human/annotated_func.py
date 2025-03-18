#State of the program right berfore the function call: a is a list of n integers (1 ≤ a_i ≤ 10^9), p is a list of n integers (1 ≤ p_i ≤ n) representing a permutation, s is a tuple containing four integers (n, k, P_B, P_S) where 1 ≤ P_B, P_S ≤ n, 1 ≤ k ≤ 10^9, and n is the length of the permutation and array a.
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
        
    #State: `mx` is the maximum value calculated during the loop, `cur` is the accumulated sum of the elements visited, `vis` is a list of `n` integers where some elements are set to 1 indicating visited states, and `s` is the last state visited before the loop terminates.
    return mx
    #The program returns `mx`, which is the maximum value calculated during the loop.
#Overall this is what the function does:The function calculates and returns the maximum value of a specific expression `cur + k * a[s]` as it iterates through a permutation of indices, updating the current sum `cur` and decrementing `k` until `k` reaches zero or a cycle is detected.

