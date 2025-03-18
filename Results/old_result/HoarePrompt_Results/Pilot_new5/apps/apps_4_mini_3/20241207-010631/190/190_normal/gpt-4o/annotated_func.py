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
        
    #State of the program after the  for loop has been executed: `min_cost` is the minimum total cost calculated based on the adjustments made for each length in list `a` relative to the best `t`, `best_t` is the value of `t` that resulted in `min_cost`, `n` is an input integer such that 1 <= n <= 1000, `a` is a list of `n` integers where each integer `a_i` is a positive integer such that 1 <= `a_i` <= 100.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts an integer `n`, which indicates the number of integers in a list, and a list `a` of `n` positive integers (1 ≤ a_i ≤ 100). It calculates the minimum adjustment cost required to transform the lengths in `a` such that they are all within one unit of an optimal target `t` (where t varies from 1 to 100). The function returns the optimal value of `t` that results in the minimum cost along with that minimum cost.

