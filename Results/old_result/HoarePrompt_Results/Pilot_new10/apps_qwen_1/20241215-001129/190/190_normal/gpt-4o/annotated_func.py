#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, and a list of n integers a where 1 ≤ a_i ≤ 100 represents the lengths of the sticks.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \( 1 \leq n \leq 1000 \), `a` is a list of integers where \( 1 \leq a_i \leq 100 \), `min_cost` is the minimum value of `current_cost` encountered during the loop execution, `best_t` is the value of `t` that gave the minimum `current_cost`, `t` is 100 (the maximum value of `t` in the loop), and `current_cost` is the final cost calculated after the loop completes.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts an integer `n` and a list of `n` integers `a`, representing the lengths of sticks. It finds the optimal value of `t` (where \(1 \leq t \leq 100\)) that minimizes the cost of cutting the sticks such that the cost is the sum of the differences between the stick lengths and the closest multiple of `t`. The function then prints the optimal `t` and the corresponding minimum cost.

