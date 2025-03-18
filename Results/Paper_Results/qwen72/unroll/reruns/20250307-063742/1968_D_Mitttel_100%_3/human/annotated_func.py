#State of the program right berfore the function call: a and p are lists of integers of the same length n (1 ≤ n ≤ 2·10^5), where 1 ≤ a_i ≤ 10^9 and 1 ≤ p_i ≤ n, and p is a permutation. s is a list of two integers [P_B, P_S] (1 ≤ P_B, P_S ≤ n) representing the starting positions of Bodya and Sasha, and k is a positive integer (1 ≤ k ≤ 10^9) representing the number of turns in the game.
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
        
    #State: The loop terminates when either `k` becomes 0 or `vis[s]` becomes 1. The final values of `mx`, `cur`, `k`, and `vis` will depend on the specific values of `a`, `p`, and the initial positions `s`.
    return mx
    #The program returns the value of `mx`, which is the maximum value encountered during the execution of the loop.
#Overall this is what the function does:The function `func_1` takes four parameters: `a` and `p` (lists of integers of the same length `n`), `s` (a list of two integers representing starting positions), and `k` (a positive integer representing the number of turns). It returns the maximum value of `cur + k * a[s]` encountered during the game, where `cur` is the cumulative sum of the elements in `a` accessed through the permutation `p`, and `k` is decremented with each turn. The game ends when either all `k` turns are used or a position in `s` is revisited.

