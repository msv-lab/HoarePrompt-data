#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000, and a is a list of n positive integers where each integer a[i] satisfies 1 <= a[i] <= 100.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer satisfying 1 <= `n` <= 1000, `a` is a list of `n` positive integers where each integer `a[i]` satisfies 1 <= `a[i]` <= 100, `min_cost` is the minimum cost calculated based on the best `t`, `best_t` is the value of `t` that results in `min_cost`.
    print(best_t, min_cost)
#Overall this is what the function does:The function reads a positive integer `n` and a list `a` of `n` positive integers. It calculates the minimum cost to adjust the numbers in the list `a` to be centered around an optimal target value `t`, which ranges from 1 to 100. The cost is defined by how much each number in `a` deviates from the range `[t-1, t+1]`. The function identifies the target value `best_t` that yields the minimum adjustment cost (`min_cost`) and prints both `best_t` and `min_cost` at the end. The code does not handle invalid input beyond the stated constraints and does not account for cases where `n` or `a` may be empty or malformed outside the range of the given assumptions.

