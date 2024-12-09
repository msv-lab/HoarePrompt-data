#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000, and a is a list of n integers where each integer represents the lengths of sticks and satisfies 1 <= a[i] <= 100 for all valid indices i.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 1000; `a` is a list containing `n` integers; `min_cost` is the minimum cost calculated based on the lengths in `a` relative to the best `t`, and `best_t` is the value of `t` that resulted in `min_cost`.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts a positive integer `n` and a list of `n` integers representing stick lengths. It calculates the minimum cost to adjust the lengths of the sticks so that they are within the range of `best_t - 1` to `best_t + 1`, for `t` values ranging from 1 to 100. The function returns the value of `best_t` that results in the minimum adjustment cost and the corresponding minimum cost itself.

