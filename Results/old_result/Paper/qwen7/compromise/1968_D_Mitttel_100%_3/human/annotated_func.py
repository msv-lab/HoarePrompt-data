#State of the program right berfore the function call: a is a list of integers representing the array a, p is a permutation of integers from 1 to n, s is a list of integers representing the starting positions (P_B, P_S) for Bodya and Sasha, and k is a positive integer representing the duration of the game.
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
        
    #State: Output State: `k` is 0, `mx` is the maximum value encountered during the loop (i.e., the maximum of `mx` and `cur + k * a[s]` for each iteration), `cur` is the final value of `cur` after the last iteration (i.e., `cur + a[s]` for the last iteration), `vis[s]` is 1, and `s` is updated to `p[s]` for the last iteration.
    #
    #In simpler terms, after the loop completes all its iterations, `k` will be 0 because it is decremented by 1 in each iteration until it reaches 0. The variable `mx` will hold the highest value between its previous value and `cur + k * a[s]` for each iteration. `cur` will be the final value it takes after the last iteration, which is `cur + a[s]`. `vis[s]` will be marked as 1 because it is set to 1 in the first line of the loop. Finally, `s` will be updated to `p[s]` for the last iteration, meaning it will hold the value of `p[s]` after the loop ends.
    return mx
    #The program returns the maximum value between `mx` and `cur + k * a[s]` for each iteration, with `k` being 0, `cur` holding the final value after the last iteration (`cur + a[s]`), `vis[s]` marked as 1, and `s` holding the value of `p[s]` after the loop ends.
#Overall this is what the function does:The function accepts a list of integers `a`, a permutation of integers `p`, a list of integers `s`, and a positive integer `k`. It iterates through the list `s` based on the permutation `p`, updating the maximum value `mx` and the current sum `cur` until `k` reaches 0. After completing the iterations, it returns the maximum value between `mx` and `cur + k * a[s]` for the last iteration.

