#State of the program right berfore the function call: p is a list of distinct positive integers sorted in ascending order, where 1 <= p[i] <= 100.
def func_1(p):
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: `p` is a list of distinct positive integers sorted in ascending order, where 1 <= p[i] <= 100; `max_n` is 100; `remaining_players` is a list of 101 integers where each element `remaining_players[n]` (for 1 <= n <= 100) is the result of the loop's computation for that `n`, specifically the largest value less than the minimum value in `p` after subtracting the count of elements in `p` that are less than or equal to `n`; `n` is 100; `cur_n` is the largest value less than the minimum value in `p`.
    return remaining_players
    #The program returns a list `remaining_players` of 101 integers, where each element `remaining_players[n]` (for 1 <= n <= 100) represents the largest value less than the minimum value in `p` after subtracting the count of elements in `p` that are less than or equal to `n`. The first element of the list is not used (index 0), and the rest of the elements are computed based on the described logic.
#Overall this is what the function does:The function `func_1` accepts a list `p` of distinct positive integers sorted in ascending order, where each integer is between 1 and 100 inclusive. It returns a list `remaining_players` of 101 integers, where each element `remaining_players[n]` (for 1 <= n <= 100) represents the largest value less than the minimum value in `p` after subtracting the count of elements in `p` that are less than or equal to `n`. The first element of the list (index 0) is not used.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 250. k and q are positive integers where 1 ≤ k, q ≤ 100, representing the length of the sequence a and the number of values n_i, respectively. p is a list of k unique integers in ascending order, where 1 ≤ p[i] ≤ 100. qs is a list of q integers, where 1 ≤ qs[i] ≤ 100.
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
        
    #State: After the loop executes all the iterations, `t` is an input integer between 1 and 250, `k` and `q` are input integers where 1 ≤ k, q ≤ 100, `p` is a list of integers read from the input, `qs` is a list of integers read from the input, `results` is a list containing `t` string elements, each of which is the space-separated string representation of the elements in `res` for each iteration, `remaining_players` is the result of `func_1(p)` for the last iteration, `res` is a list containing the elements of `remaining_players` at the indices specified by `qs` for the last iteration.
    return results
    #The program returns a list `results` containing `t` string elements, where each element is a space-separated string representation of the elements in `res` for each iteration. Here, `t` is an input integer between 1 and 250, and `res` is a list containing the elements of `remaining_players` at the indices specified by `qs` for the last iteration. `remaining_players` is the result of `func_1(p)` for the last iteration, where `p` is a list of integers read from the input.
#Overall this is what the function does:The function `func_2` reads input values for `t`, `k`, `q`, `p`, and `qs` to process `t` test cases. For each test case, it generates a list `res` by selecting elements from the list `remaining_players` (which is the result of calling `func_1(p)`) at the indices specified by `qs`. The function returns a list `results` containing `t` string elements, where each element is a space-separated string representation of the elements in `res` for the corresponding test case.

