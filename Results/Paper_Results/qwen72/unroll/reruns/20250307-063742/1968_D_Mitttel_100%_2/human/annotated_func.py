#State of the program right berfore the function call: a and p are lists of integers of the same length n, where 1 ≤ n ≤ 2·10^5, s is a tuple of two integers (P_B, P_S) such that 1 ≤ P_B, P_S ≤ n, and k is a positive integer such that 1 ≤ k ≤ 10^9. The elements of p form a permutation of integers from 1 to n, and the elements of a are positive integers such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: The loop modifies the values of `vis`, `mx`, `cur`, and `k` based on the initial state and the loop's logic.
    return mx
    #The program returns the final value of `mx`, which is the maximum value that `cur` has reached during the execution of the loop.
#Overall this is what the function does:The function `func_1` takes four parameters: `a` (a list of positive integers), `p` (a list of integers forming a permutation from 1 to n), `s` (a tuple of two integers (P_B, P_S)), and `k` (a positive integer). It returns the maximum value that can be computed by adding `k` times the value of `a[s]` to a running sum `cur`, while decrementing `k` and updating `s` to `p[s]` until either `k` reaches 0 or a cycle is detected in the permutation `p`. The final state of the program includes the modified `vis` list (indicating visited indices), the final value of `cur`, and the remaining value of `k`, but the function only returns the maximum value `mx` that was computed during the process.

