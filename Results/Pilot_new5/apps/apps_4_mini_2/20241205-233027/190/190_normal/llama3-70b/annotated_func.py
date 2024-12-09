#State of the program right berfore the function call: n is an integer between 1 and 1000, and a is a list of n integers where each integer is between 1 and 100.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000, `sticks` is a sorted list of integers derived from `a`, `mid` is at least `1`, `min_cost` is the minimum cost calculated for the best `t`, and `min_t` is the value of `t` that yielded `min_cost`.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000, `sticks` is a sorted list of integers derived from `a`, `mid` is at least `1`, `min_cost` is the minimum cost calculated across all `i` from `mid + 1` to `100`, `min_t` is the value of `i` that yielded `min_cost`, `i` is `101` after the loop execution ends, and `cost` is the sum of min(abs(x - 101), abs(x - 100)) for x in `sticks` at the last iteration, if `cost` was less than `min_cost` before the loop concluded, `min_cost` and `min_t` would have been updated accordingly. If `mid` is `100` or greater, then the loop does not execute and `min_cost` remains unchanged from its initial value, `min_t` remains unchanged from its initial value.
    print(min_t, min_cost)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 1000) and a list of `n` integers (1 ≤ a[i] ≤ 100). It calculates the minimum cost to align all stick lengths to a single value `t`, where `t` can be any integer from 1 to 100. The function finds the optimal `t` that results in the lowest cost, defined as the sum of the absolute differences between each stick length and `t`. Finally, it prints the optimal `t` and the corresponding minimum cost. If `n` is 0 or if the list is not properly formed, the function’s behavior might be undefined, as it does not handle such edge cases.

