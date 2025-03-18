#State of the program right berfore the function call: a and p are lists of integers of the same length n (1 ≤ n ≤ 2·10^5), where each element of p is a distinct integer from 1 to n, and each element of a is an integer (1 ≤ a_i ≤ 10^9). s is a list of two integers [P_B, P_S] representing the starting positions of Bodya and Sasha, respectively, where 1 ≤ P_B, P_S ≤ n. k is a positive integer (1 ≤ k ≤ 10^9) representing the number of turns in the game.
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
        
    #State: The loop terminates when either `k` reaches 0 or `vis[s]` becomes 1. At this point, `a` and `p` remain unchanged, `s` is the position where the loop terminates, `k` is the remaining number of turns (which could be 0), `n` remains unchanged, `mx` is the maximum value of `cur + k * a[s]` observed during the loop execution, `cur` is the sum of the elements of `a` at the positions visited during the loop, and `vis` is a list where the elements at the positions visited by the loop are set to 1.
    return mx
    #The program returns the maximum value of `cur + k * a[s]` observed during the loop execution, where `cur` is the sum of the elements of `a` at the positions visited during the loop, `k` is the remaining number of turns (which could be 0), and `a[s]` is the element of the list `a` at the position `s` where the loop terminates.
#Overall this is what the function does:The function `func_1` takes four parameters: `a` (a list of integers), `p` (a list of distinct integers), `s` (a list of two integers representing starting positions), and `k` (a positive integer representing the number of turns). It returns the maximum value of `cur + k * a[s]` observed during the loop execution, where `cur` is the cumulative sum of the elements of `a` at the positions visited during the loop, `k` is the remaining number of turns (which could be 0), and `a[s]` is the element of the list `a` at the position `s` where the loop terminates. The function does not modify the input lists `a` and `p`, but it updates the position `s` and the number of turns `k` as it progresses through the loop. The list `vis` is used to track visited positions, and its elements are set to 1 for the positions visited during the loop.

