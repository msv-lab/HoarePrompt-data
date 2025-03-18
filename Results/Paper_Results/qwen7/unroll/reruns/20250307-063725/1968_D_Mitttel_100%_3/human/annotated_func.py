#State of the program right berfore the function call: a is a list of integers representing the array a, p is a permutation of integers from 1 to n, s is a list of two integers representing the starting positions of Bodya and Sasha, and k is a positive integer representing the duration of the game.
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
        
    #State: The output state will be `cur` equal to the sum of `a[s]` for all steps taken, `mx` equal to the maximum value of `cur + k * a[s]` encountered during the loop, `vis[s]` equal to 1 indicating the position `s` has been visited, and `k` equal to 0 as it has been decremented to 0 in the loop.
    return mx
    #The program returns the maximum value of 'cur + k * a[s]' encountered during the loop, where 'cur' is the sum of 'a[s]' for all steps taken, 'k' is 0, and 'vis[s]' indicates that position 's' has been visited.
#Overall this is what the function does:The function accepts a list of integers `a`, a permutation of integers from 1 to n `p`, a list of two integers `s` representing the starting positions, and a positive integer `k` representing the duration of the game. It traverses through the permutation starting from the given positions, updating the current sum (`cur`) and the maximum value (`mx`) of `cur + k * a[s]` encountered during the traversal. Once `k` reaches 0 or all positions have been visited, it returns the maximum value of `cur + k * a[s]` found.

