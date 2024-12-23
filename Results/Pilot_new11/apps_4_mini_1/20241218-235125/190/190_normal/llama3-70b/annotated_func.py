#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, and a is a list of n integers where each integer satisfies 1 <= a[i] <= 100.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 <= n <= 1000), `a` is a list of `n` integers (1 <= a[i] <= 100), `sticks` is a sorted list of integers, `mid` is at least 1, `i` is 0 or less, `min_cost` is the minimum sum of absolute differences of `sticks` from `t` for all valid values of `i`, and `min_t` is the value of `t` (the final value of `i` for which `min_cost` was updated) where the loop may not have executed if `mid` is equal to 1. If the loop did not execute, `min_cost` and `min_t` retain their initial values based on the original `cost` and `t`.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 <= n <= 1000), `a` is a list of `n` integers (1 <= a[i] <= 100), `sticks` is a sorted list of integers, `mid` is less than 100, `i` is 101, `min_cost` is the minimum cost calculated over the range of i (from mid+1 to 100), and `min_t` is the value of `i` that resulted in `min_cost`. If `mid` is 100 or more, `min_cost` and `min_t` remain their original values.
    print(min_t, min_cost)
#Overall this is what the function does:The function takes an integer `n` and a list of `n` integers (representing lengths of sticks) as input. It calculates the optimal length `min_t` that minimizes the total cost of transforming all stick lengths to that length, where the cost is defined as the sum of the absolute differences between the stick lengths and the target length. It performs this by evaluating costs for lengths in two ranges: from one less than the median length (the middle value of sorted sticks) down to 1, and from one more than the median length up to 100. The function ultimately prints `min_t` and the associated minimum cost `min_cost`. Edge cases include situations where the input list is already composed of identical values, and handling the cases where the median is 1 or 100, potentially resulting in empty loops if no valid `i` exists in the specified range. Notably, the function does not return a value but instead prints the results.

