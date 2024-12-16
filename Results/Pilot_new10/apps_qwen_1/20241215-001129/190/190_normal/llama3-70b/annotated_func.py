#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, and a is a list of n integers such that 1 ≤ a_i ≤ 100 for each i.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000, `sticks` is a sorted list of `n` integers, `t` is the element at index `n // 2` in the list `sticks`, `min_cost` is the minimum possible sum of the minimum absolute differences between each element in `sticks` and its adjacent elements, `min_t` is the value of `i` that achieves this minimum cost.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `i` is the value that minimizes the cost in the range `[mid + 1, 100]`, `min_cost` is the minimum possible sum of the minimum absolute differences for any `i` in the range, and `min_t` is the value of `i` that achieves this minimum cost.
    print(min_t, min_cost)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers `a` from the input. It then sorts the list and finds the median value. The function calculates the minimum cost of adjusting all elements in the list to either the median or one of its neighboring values. It iterates over the range `[median - 1, 0]` and `[median + 1, 100]` to find the value that minimizes the cost, and prints the optimal value and the corresponding minimum cost.

