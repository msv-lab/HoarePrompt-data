#State of the program right berfore the function call: n is an integer between 1 and 1000, and a is a list of integers where each integer represents the length of a stick, with each length being a positive integer between 1 and 100.
def func():
    n = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    mid = sticks[n // 2]
    cost = sum(abs(x - mid) for x in sticks)
    t = mid
    min_cost = cost
    min_t = t
    for i in range(mid - 1, 0, -1):
        cost = sum(min(abs(x - i), abs(x - (i + 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000; `a` is a sorted list of integers; if the loop executed, `min_cost` is the minimum cost found, `min_t` is the corresponding value of `t` that minimized the cost; otherwise, if the loop did not execute, `min_cost` remains equal to the initial `cost` and `min_t` is equal to `mid`.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000, `a` is a sorted list of integers, `min_cost` is the minimum cost found after evaluating all possible values of `i` from `mid + 1` to 100, and `min_t` is the corresponding value of `t` that minimized the cost; if the loop did not execute, `min_cost` remains equal to the initial `cost` and `min_t` is equal to `mid`.
    print(min_t, min_cost)
#Overall this is what the function does:The function accepts an integer `n` (between 1 and 1000) and a list `sticks` of `n` positive integers (each between 1 and 100) that represent stick lengths. It finds the optimal stick length `min_t` between 1 and 100 that minimizes the total cost of adjusting all sticks to that length, where the cost is defined as the sum of the absolute differences between each stick and the optimal length. It returns the optimal length `min_t` along with the associated minimum cost `min_cost` of adjustment.

