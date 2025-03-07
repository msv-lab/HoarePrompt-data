#State of the program right berfore the function call: a and p are lists of integers of the same length n (1 ≤ n ≤ 2 · 10^5), where each element in p is a unique integer from 1 to n, and each element in a is a positive integer (1 ≤ a_i ≤ 10^9). s is a list of two integers representing the starting positions of Bodya and Sasha (1 ≤ s[0], s[1] ≤ n). k is a positive integer representing the number of turns in the game (1 ≤ k ≤ 10^9).
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
        
    #State: The loop has finished executing, and the following changes have occurred: `s` is now the position in `p` that was last visited before the loop terminated. `k` is 0 or the number of remaining turns that were not executed because the position `s` was already visited. `mx` is the maximum value calculated during the loop, which is the greatest value of `cur + k * a[s]` encountered. `cur` is the cumulative sum of the elements in `a` that were visited during the loop. `vis` is a list of `n` integers where each visited position in `p` has a value of 1, and all other positions remain 0. The lists `a` and `p` remain unchanged, and `n` is still the length of the list `p`.
    return mx
    #The program returns the maximum value `mx` calculated during the loop, which is the greatest value of `cur + k * a[s]` encountered.
#Overall this is what the function does:The function `func_1` accepts four parameters: `a` (a list of positive integers), `p` (a list of unique integers from 1 to n), `s` (a list of two integers representing starting positions), and `k` (a positive integer representing the number of turns). It returns the maximum value of `cur + k * a[s]` encountered during the loop, where `cur` is the cumulative sum of the elements in `a` that were visited, and `s` is updated based on the elements in `p`. The function ensures that each position in `p` is visited at most once, and the lists `a` and `p` remain unchanged. After the function concludes, `s` is the last position visited, `k` is 0 or the remaining turns that were not executed due to a repeated position, and `mx` is the maximum value calculated.

