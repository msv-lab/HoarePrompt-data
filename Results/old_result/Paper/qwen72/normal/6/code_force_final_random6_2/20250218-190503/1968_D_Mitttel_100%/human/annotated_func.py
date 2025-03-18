#State of the program right berfore the function call: a and p are lists of integers of the same length n, where 1 <= n <= 2 * 10^5, 1 <= a[i] <= 10^9, and p is a permutation of integers from 1 to n. s is a list of two integers representing the starting positions of Bodya and Sasha, where 1 <= s[0], s[1] <= n. k is a positive integer such that 1 <= k <= 10^9.
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
        
    #State: The loop terminates when either `vis[s]` is 1 or `k` is 0. At this point, `mx` will be the maximum value of `cur + k * a[s]` encountered during the loop execution. `cur` will be the sum of `a[s]` for each position `s` visited in the loop. `k` will be the remaining number of iterations, which is 0 if the loop terminated due to `k` reaching 0, or a positive integer if the loop terminated due to `vis[s]` being 1. `vis` will be a list of length `n` where each element visited by `s` during the loop will be 1, and all other elements will remain 0.
    return mx
    #The program returns the maximum value of `cur + k * a[s]` encountered during the loop execution, where `cur` is the sum of `a[s]` for each position `s` visited in the loop, `k` is the remaining number of iterations, and `a[s]` is the value at position `s` in the list `a`.
#Overall this is what the function does:The function `func_1` takes four parameters: `a` (a list of integers), `p` (a permutation of integers from 1 to n), `s` (a list of two integers representing starting positions), and `k` (a positive integer). It returns the maximum value of `cur + k * a[s]` encountered during the loop execution, where `cur` is the sum of `a[s]` for each position `s` visited, `k` is the remaining number of iterations, and `a[s]` is the value at position `s` in the list `a`. The loop terminates when either a position in `s` is revisited (i.e., `vis[s]` is 1) or `k` reaches 0. After the function concludes, `mx` holds the maximum value computed, `cur` is the sum of `a[s]` for all visited positions, `k` is the remaining number of iterations, and `vis` is a list indicating which positions in `p` have been visited.

