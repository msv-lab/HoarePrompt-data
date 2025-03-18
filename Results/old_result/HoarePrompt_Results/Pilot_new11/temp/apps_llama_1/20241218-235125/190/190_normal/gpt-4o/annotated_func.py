#State of the program right berfore the function call: The input consists of a single integer n (1 <= n <= 1000) representing the number of sticks, followed by n integers a_i (1 <= a_i <= 100) representing the lengths of the sticks.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000 (inclusive), `a` is a list of integers, `min_cost` is the minimum cost achievable by adjusting lengths in `a` to be within 1 unit of `t` for `t` in the range 1 to 101, and `best_t` is the value of `t` that achieves `min_cost`.
    print(best_t, min_cost)
#Overall this is what the function does:The function calculates the optimal target length (`best_t`) and the corresponding minimum cost (`min_cost`) for adjusting a list of stick lengths to be within 1 unit of the target length, based on input values for the number of sticks and their lengths. It accepts no parameters, operates on predefined input values, and returns the calculated `best_t` and `min_cost` as output. The function handles stick lengths between 1 and 100 and considers target lengths from 1 to 100. It calculates the minimum cost by summing the adjustments needed for each stick to reach the target length, considering cases where the stick length is less than or greater than the target length. The function covers all potential edge cases, including stick lengths at the boundaries (1 and 100) and target lengths at the boundaries (1 and 100). After execution, the program state includes the optimal target length (`best_t`) and the corresponding minimum cost (`min_cost`), which are printed as output.

