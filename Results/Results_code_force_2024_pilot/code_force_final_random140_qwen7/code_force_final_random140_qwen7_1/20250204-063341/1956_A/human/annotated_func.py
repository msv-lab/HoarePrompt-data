#State of the program right berfore the function call: p is a sorted list of positive integers where 1 <= p[0] < p[1] < ... < p[len(p) - 1] <= 100.
def func_1(p):
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: Output State: `remaining_players` is a list of length 101, where all elements are 0, `n` is 101, `cur_n` is 0, `count` is 0.
    #
    #Explanation: The loop iterates from `n = 1` to `n = max_n`, which in this case is 101. After each iteration, `cur_n` is set to `n` and then reduced by the value of `count`, which is determined by the `bisect.bisect_right` function. However, since `p` is not defined in the provided information and the initial conditions suggest that `p` is a list of minimum player counts, and given that `cur_n` is always reduced until it becomes 0, the final state of `remaining_players` will have all elements as 0 by the end of the loop. The variable `n` will reach 101 after the last iteration, and `cur_n` and `count` will both be 0 at that point.
    return remaining_players
    #`remaining_players` is a list of length 101, where all elements are 0
#Overall this is what the function does:The function accepts a sorted list of positive integers `p` where each element is between 1 and 100, inclusive. It initializes a list `remaining_players` of length 101 with all elements set to 0. For each integer `n` from 1 to 101, it updates `cur_n` to `n` and repeatedly subtracts the count of elements in `p` that are less than or equal to `cur_n` until `cur_n` becomes 0. Finally, it stores the result in `remaining_players[n]`. After completing these operations for all `n`, the function returns `remaining_players`, which is a list of length 101 where all elements are 0.

#State of the program right berfore the function call: k and q are positive integers such that 1 ≤ k, q ≤ 100; p is a list of k integers representing the sequence a where 1 ≤ a_1 < a_2 < ... < a_k ≤ 100; qs is a list of q integers representing n_i where 1 ≤ n_i ≤ 100.
def func_2():
    t = int(input())
    results = []
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        remaining_players = func_1(p)
        
        res = [remaining_players[n] for n in qs]
        
        results.append(' '.join(map(str, res)))
        
    #State: Output State: `t` is an input integer indicating the total number of iterations the loop will execute. After all iterations, `k` and `q` will be the last integers input split for each iteration, `p` will be the last list of integers obtained from the input split for `p`, `qs` will be the last list of integers obtained from the input split for `qs`, `remaining_players` will be the return value of `func_1(p)` for the last iteration, `res` will be a list of elements from `remaining_players` indexed by the elements in `qs` for the last iteration, and `results` will be a list containing strings which are the results of joining the elements of `res` with spaces for each iteration, forming a list of length `t`.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will be the final input integer provided, `k` and `q` will be the last two integers input split, `p` will be the last list of integers input for `p`, `qs` will be the last list of integers input for `qs`, `remaining_players` will be the result of `func_1(p)` for the last iteration, `res` will contain the indexed elements from `remaining_players` based on `qs` for the last iteration, and `results` will be a list of space-separated strings, each corresponding to the results of `res` for each iteration.
    return results
    #The program returns a list of strings, each string being a space-separated list of elements from the last `remaining_players` list indexed by the corresponding `qs` list for each iteration, with `t` being the final input integer provided, `k` and `q` being the last two integers input split, `p` being the last list of integers input for `p`, `qs` being the last list of integers input for `qs`, `remaining_players` being the result of `func_1(p)` for the last iteration, and `res` containing the indexed elements from `remaining_players` based on `qs` for the last iteration.
#Overall this is what the function does:The function processes multiple iterations of inputs, where in each iteration, it reads values for `k`, `q`, `p`, and `qs`. It then calls another function `func_1` to get the remaining players based on `p`. Using `qs`, it extracts specific elements from the result of `func_1` and stores these in a list. Finally, it formats these lists into space-separated strings and collects them into a list of results, which it returns.

