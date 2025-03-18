#State of the program right berfore the function call: a and p are lists of integers of the same length n (1 ≤ n ≤ 2·10^5), where 1 ≤ a_i ≤ 10^9 and 1 ≤ p_i ≤ n. s is a list of two integers [P_B, P_S] representing the starting positions of Bodya and Sasha, respectively, such that 1 ≤ P_B, P_S ≤ n. k is a positive integer such that 1 ≤ k ≤ 10^9.
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
        
    #State: The loop will terminate when either `k` becomes 0 or `vis[s]` becomes 1. The final values of `vis`, `mx`, `cur`, and `k` will depend on the specific values of `a`, `p`, `s`, and the initial `k`.
    return mx
    #The program returns the value of `mx`, which is the maximum value encountered during the execution of the loop, based on the specific values of `a`, `p`, `s`, and the initial `k`.
#Overall this is what the function does:The function `func_1` accepts four parameters: `a` (a list of integers), `p` (a list of integers), `s` (a list of two integers representing starting positions), and `k` (a positive integer). It returns the maximum value encountered during the execution of a loop, which is calculated as the maximum of `cur + k * a[s]` at each iteration, where `cur` is the cumulative sum of elements in `a` accessed by the positions in `p` starting from the positions in `s`, and `k` is decremented with each iteration. The loop terminates when either `k` becomes 0 or a position in `s` is revisited (i.e., `vis[s]` becomes 1). The function does not modify the input parameters `a`, `p`, or `s`, but it updates the internal state variables `vis`, `mx`, `cur`, and `k`.

