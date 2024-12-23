#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
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
        
    #State of the program after the  for loop has been executed: `min_t` is the value of `i` that minimizes the cost, `min_cost` is the minimum cost found, `sticks` is a sorted list of `n` integers, `t` is equal to `mid`, and `cost` is the initial cost.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `i` is `100`, `min_t` is the value of `i` that minimizes the cost, `min_cost` is the minimum cost found, `sticks` is a sorted list of `n` integers, `t` is equal to `mid`, and `cost` is the last calculated cost when `i` is `100`.
    print(min_t, min_cost)
#Overall this is what the function does:The function reads a list of integers `a` of length `n` (where `1 ≤ n ≤ 1000`) and each integer `a_i` in the list satisfies `1 ≤ a_i ≤ 100`. It then sorts the list and calculates the median value `mid`. The function computes the cost of moving all elements in the list to a central value by considering the median and values around the median. Specifically, it first checks the cost for values around the median (`mid - 1` to `0` and `mid + 1` to `100`). The function finds the central value `min_t` that minimizes the total cost of moving all elements to that value. Finally, it prints the optimal central value `min_t` and the corresponding minimum cost `min_cost`.

Potential edge cases and missing functionality:
- The function handles the case where the median `mid` is considered initially, but it does not handle the case where the median itself is one of the elements in the list. This could potentially affect the cost calculation.
- The function assumes that the input values are within the specified range (1 to 100). If the input includes values outside this range, the function would still run but might produce incorrect results.
- The function does not check for duplicate values in the input list, which might affect the cost calculation if multiple elements have the same value as the median or the optimal central value.

