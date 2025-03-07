#State of the program right berfore the function call: a is a list of n integers (1 ≤ a_i ≤ 10^9), p is a list of n integers (1 ≤ p_i ≤ n) representing a permutation, s is a list of 4 integers [t, n, P_B, P_S] where t is the number of test cases (1 ≤ t ≤ 10^4), n is the length of the permutation (1 ≤ n ≤ 2·10^5), P_B and P_S are the starting positions of Bodya and Sasha respectively (1 ≤ P_B, P_S ≤ n), and k is the number of turns in the game (1 ≤ k ≤ 10^9). The sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: `vis` is a list of n integers where positions corresponding to the visited indices are 1, `mx` is the maximum value of `cur + k * a[s]` encountered, `cur` is the sum of `a[s]` values accumulated, `s` is the last visited position, and `k` is 0 if all turns were used or the remaining turns if a cycle was detected.
    return mx
    #The program returns mx, which is the maximum value of cur + k * a[s] encountered.
#Overall this is what the function does:The function calculates and returns the maximum value of `cur + k * a[s]` encountered, where `cur` is the cumulative sum of values from list `a` based on the permutation in list `p`, starting from the position `s`, and `k` is the number of turns available.

