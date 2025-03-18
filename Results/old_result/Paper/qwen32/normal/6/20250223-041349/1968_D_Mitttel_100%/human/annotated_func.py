#State of the program right berfore the function call: a is a list of n integers where each integer is between 1 and 10^9 inclusive, p is a list of n integers representing a permutation of length n where each integer is between 1 and n inclusive, s is a tuple containing four integers (t, n, P_B, P_S) where t is the number of test cases (1 ≤ t ≤ 10^4), n is the length of the permutation (1 ≤ n ≤ 2·10^5), P_B and P_S are the starting positions of Bodya and Sasha respectively (1 ≤ P_B, P_S ≤ n), and k is the duration of the game (1 ≤ k ≤ 10^9). The sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: vis is a list where vis[i] is 1 for all visited positions i, mx is the maximum value of cur + k * a[s] encountered, cur is the cumulative sum of a[s] for all visited positions, k is the remaining duration of the game, and s is the last visited position before termination.
    return mx
    #The program returns mx, which is the maximum value of cur + k * a[s] encountered.
#Overall this is what the function does:The function calculates and returns the maximum value of `cur + k * a[s]` encountered during the traversal of a permutation `p` starting from position `s`, where `cur` is the cumulative sum of elements from `a` at visited positions, and `k` is decremented by 1 at each step until it reaches 0 or a position is revisited.

