#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000, and a is a list of n integers where each integer a_i is a positive integer such that 1 <= a_i <= 100.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 <= n <= 1000), `a` is a list of `n` integers (1 <= `a_i` <= 100), `min_cost` is the minimum cost computed across all iterations, `best_t` is the value of `t` that provides the minimum cost.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts a positive integer `n`, which represents the number of integers in a list `a`, and reads a list of `n` positive integers from input. It calculates the minimum cost to adjust the integers in `a` such that they fall within the range `[t - 1, t + 1]` for values of `t` from 1 to 100. The function then returns the value of `t` that results in the minimum cost and the corresponding minimum cost itself.

