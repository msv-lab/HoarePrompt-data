#State of the program right berfore the function call: p is a list of integers such that 1 <= p[0] < p[1] < ... < p[k-1] <= 100, where k is the length of p.
def func_1(p):
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: After all iterations, `p` remains a list of integers such that 1 <= p[0] < p[1] < ... < p[k-1] <= 100, `max_n` is 100, `remaining_players` is a list where each element at index `n` (1 to 100) is the final value of `cur_n` after processing that iteration, and `n` is 100.
    return remaining_players
    #The program returns a list `remaining_players` where each element at index `n` (from 1 to 100) represents the final value of `cur_n` after processing that iteration.
#Overall this is what the function does:The function `func_1` takes a list `p` of unique integers sorted in ascending order, where each integer is between 1 and 100. It processes each integer from 1 to 100, reducing it based on the values in `p`, and returns a list `remaining_players` where each element at index `n` (from 1 to 100) represents the final value of `cur_n` after processing that iteration. The original list `p` remains unchanged.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 250. k and q are positive integers representing the length of the sequence `a` and the number of values `n_i` to solve for, respectively, where 1 ≤ k, q ≤ 100. p is a list of k integers in strictly increasing order, where 1 ≤ p[0] < p[1] < ... < p[k-1] ≤ 100. qs is a list of q integers, where 1 ≤ qs[i] ≤ 100 for all 0 ≤ i < q.
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
        
    #State: `t` must be greater than or equal to the number of iterations, `_` is `t - 1`, `k` and `q` are integers provided by the user, `p` is a list of integers provided by the user, `qs` is a list of integers provided by the user, `remaining_players` is the result of `func_1(p)`, `res` is a list containing elements from `remaining_players` at indices specified by `qs`, `results` contains `t` elements, each of which is a string formed by joining the string representations of the elements in `res` with spaces.
    return results
    #The program returns a list `results` containing `t` elements, where each element is a string formed by joining the string representations of the elements in `res` with spaces. `res` is a list containing elements from `remaining_players` at indices specified by `qs`. `remaining_players` is the result of `func_1(p)`, and `p` is a list of integers provided by the user. `qs` is a list of integers provided by the user, and `t` is an integer greater than or equal to the number of iterations.
#Overall this is what the function does:The function `func_2` reads multiple sets of input data, processes each set, and returns a list of results. Each set of input data includes the length of a sequence `p`, a list of integers `p`, and a list of query indices `qs`. For each set, the function computes a new list `remaining_players` by calling `func_1(p)`, then selects elements from `remaining_players` based on the indices in `qs`. These selected elements are converted to strings and concatenated into a single string, which is added to the final list `results`. After processing all sets, the function returns `results`, a list of `t` strings, where each string represents the concatenated results of the corresponding set of queries.

