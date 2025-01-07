#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000, and a is a list of n integers where each integer a_i is a positive integer such that 1 <= a_i <= 100.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 1000; `a` is a list of `n` integers where each integer `a_i` is a positive integer such that 1 <= `a_i` <= 100; `sticks` is a sorted list of `n` integers; `mid` is the element at index `n // 2` in `sticks`; `min_cost` is the minimum cost computed over all values of `i` from `mid - 1` down to 1; `min_t` is the value of `i` that resulted in `min_cost`; `t` remains equal to the original value of `mid`.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 1000; `a` is a list of `n` positive integers where each integer `a_i` is a positive integer such that 1 <= `a_i` <= 100; `sticks` is a sorted list of `n` integers; `mid` is less than or equal to 99; `min_cost` is the minimum computed cost across all values of `i` from `mid + 1` to 100; `min_t` is the value of `i` that resulted in `min_cost`; `t` remains equal to the original value of `mid`.
    print(min_t, min_cost)
#Overall this is what the function does:The function accepts an integer `n` (1 <= n <= 1000) and a list of `n` positive integers (1 <= a_i <= 100). It computes the value `t` that minimizes the total cost of adjusting each integer in the list to `t`, where the cost is defined as the sum of the absolute differences between each integer and `t`. The function considers values of `t` from `mid - 1` down to 1 and from `mid + 1` up to 100, where `mid` is the median value of the sorted list. Finally, it prints the optimal value of `t` that results in the minimum cost along with that minimum cost.

