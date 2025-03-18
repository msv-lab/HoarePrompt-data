#State of the program right berfore the function call: p is a sorted list of integers where 1 <= p[0] < p[1] < ... < p[-1] <= 100, and the length of p is k (1 <= k <= 100).
def func_1(p):
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: Output State: After the loop executes all its iterations, `remaining_players` will be a list where each element `remaining_players[n]` is calculated as follows: For each `n` from 1 to `max_n`, the variable `cur_n` starts with the value of `n` and repeatedly decreases by the count of elements in `p` that are less than or equal to `cur_n` until `cur_n` is less than `min(p)`. The final value of `cur_n` is assigned to `remaining_players[n]`.
    #
    #In simpler terms, after all iterations of the loop, `remaining_players` will contain the final value of `cur_n` for each `n` from 1 to `max_n`, which represents how much `n` would decrease by following the described process until it falls below the minimum value in `p`.
    return remaining_players
    #remaining_players is a list where each element remaining_players[n] is the final value of cur_n after it has been repeatedly decreased by the count of elements in p that are less than or equal to cur_n, until cur_n is less than the minimum value in p for each n from 1 to max_n.
#Overall this is what the function does:The function accepts a sorted list of integers `p` where each integer is between 1 and 100, and returns a list `remaining_players`. Each element `remaining_players[n]` in the returned list is the final value of `cur_n` after it has been repeatedly decreased by the count of elements in `p` that are less than or equal to `cur_n`, until `cur_n` is less than the minimum value in `p` for each `n` from 1 to the maximum value in `p`.

#State of the program right berfore the function call: k and q are positive integers such that 1 ≤ k, q ≤ 100; p is a list of k positive integers in strictly increasing order such that 1 ≤ p[i] ≤ 100 for all 0 ≤ i < k; qs is a list of q positive integers such that 1 ≤ n_i ≤ 100 for all 0 ≤ i < q.
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
        
    #State: Output State: `k` is an integer input from the last iteration's first split, `q` is an integer input from the last iteration's second split, `p` is a list of integers obtained from the last iteration's third input split, `qs` is a list of integers obtained from the last iteration's fourth input split, `remaining_players` is the result of `func_1(p)` from the last iteration, `res` is a list of elements from `remaining_players` indexed by the elements in `qs`, `results` is a list containing string representations of `res` joined by spaces from all iterations, `t` is a positive integer reduced by the number of iterations completed, which is now 0 since all iterations have been executed.
    #
    #In simpler terms, after all iterations of the loop have finished, `k` and `q` will hold the values from the last set of inputs provided, `p` and `qs` will contain the last lists of integers, `remaining_players` will be the result of `func_1(p)` for the last iteration, `res` will be the list of elements from `remaining_players` indexed by `qs`, and `results` will be a list of strings, each representing the `res` list from each iteration, joined by spaces. The variable `t` will be 0 as all iterations have been completed.
    return results
    #The program returns a string that is a space-separated list of string representations of the `res` list from each iteration, where `res` is a list of elements from `remaining_players` indexed by the elements in `qs`. The last set of inputs provided resulted in `k` being an integer, `q` being an integer, `p` being a list of integers, `qs` being a list of integers, `remaining_players` being the result of `func_1(p)`, and `res` being a list of elements from `remaining_players` indexed by `qs`.
#Overall this is what the function does:The function processes multiple sets of inputs, each consisting of integers k, q, a list p of k integers, and a list qs of q integers. For each set, it calls another function `func_1` to get the remaining players based on the list p, then extracts specific players indicated by qs. It collects these extracted lists into a results list, converts each list to a space-separated string, and finally returns a single string containing all these results concatenated together.

