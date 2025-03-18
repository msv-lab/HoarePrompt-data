#State of the program right berfore the function call: a is a list of integers representing the array a, p is a permutation of integers from 1 to n, s is a list of integers representing the starting positions (P_B, P_S) for Bodya and Sasha, and k is a non-negative integer representing the duration of the game.
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
        
    #State: Output State: `mx` is the maximum value encountered during all iterations of the loop, `cur` is the sum of `a[s]` accumulated during all iterations, `k` is 0 (since it is decremented until it reaches 0), `vis[s]` is 1 if `s` was visited during any iteration, otherwise it remains 0, and `s` is updated to `p[s]` after each iteration until the condition `not vis[s] and k > 0` no longer holds.
    #
    #This means that after all iterations, `mx` will hold the highest value of `cur + k * a[s]` seen during any iteration, `cur` will be the total sum of `a[s]` added across all iterations, `k` will be 0 as it gets decremented to 0, `vis[s]` will be marked as 1 for any `s` that was visited, and `s` will point to its final value after the last iteration where the loop condition was still met.
    return mx
    #The program returns the maximum value of `cur + k * a[s]` encountered during all iterations of the loop, where `cur` is the sum of `a[s]` accumulated during all iterations, `k` is 0, `vis[s]` is marked as 1 for any `s` that was visited, and `s` points to its final value after the last iteration where the loop condition was still met.
#Overall this is what the function does:The function accepts a list of integers `a`, a permutation `p`, a list of starting positions `s`, and a non-negative integer `k`. It iterates through the list `a` based on the permutation `p` starting from the positions specified in `s`. During each iteration, it calculates the value of `cur + k * a[s]` and updates the maximum value found (`mx`). It also keeps track of visited positions in the `vis` list. After all iterations, it returns the maximum value found (`mx`).

