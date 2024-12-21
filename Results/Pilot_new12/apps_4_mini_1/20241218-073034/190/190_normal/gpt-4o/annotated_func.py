#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000, and a is a list of n integers where each integer is a positive integer such that 1 <= a[i] <= 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    min_cost = float('inf')
    best_t = -1
    for t in range(1, 101):
        current_cost = 0
        
        for length in a:
            if length < t - 1:
                current_cost += t - 1 - length
            elif length > t + 1:
                current_cost += length - (t + 1)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_t = t
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a list of `n` positive integers, `min_cost` is the minimum cost calculated for the optimal adjustment of lengths in `a`, `best_t` is the value of `t` that resulted in that minimum cost.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` positive integers. It computes the minimum cost required to adjust the lengths of the integers in list `a` to be within the range `t - 1` to `t + 1` for some value of `t` between 1 and 100. The function identifies the optimal value of `t` that results in this minimum cost and prints both the optimal `t` and the corresponding minimum cost. It operates under the assumption that `n` is always between 1 and 1000 and each integer in `a` is between 1 and 100. Despite ensuring valid inputs, the function does not handle invalid inputs or erroneous cases, such as non-integer inputs or inputs outside the expected range.

