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
        
    #State: mx is the maximum value between its original value (0) and the sum of cur plus k times a[s], considering all iterations; cur is the cumulative sum of a[s] from the start until the last iteration where k becomes 0 or vis[s] becomes 1; k is 0; s is the final node index where the loop exits.
    return mx
    #The program returns mx, which is the maximum value between its original value (0) and the sum of cur plus k times a[s], considering all iterations.
#Overall this is what the function does:The function accepts a list of integers `a`, a permutation of integers from 1 to n `p`, a list of integers `s` representing starting positions, and a positive integer `k` representing the duration of the game. It iterates through the list `a` starting from the positions specified in `s`, updating a cumulative sum `cur` and a maximum value `mx`. After considering all iterations based on the condition that `k` remains positive and the position `s` has not been visited, it returns the maximum value between its original value (0) and the sum of `cur` plus `k` times `a[s]`.

