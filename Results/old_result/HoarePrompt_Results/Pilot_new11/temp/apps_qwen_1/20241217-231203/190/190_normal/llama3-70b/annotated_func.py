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
        
    #State of the program after the  for loop has been executed: 
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: To determine the final output state of the given loop, let's break down the loop logic and the changes it makes to the variables involved.
    #
    #### Initial State
    #- `mid` is an integer.
    #- `cost` is initially undefined.
    #- `min_cost` is initially undefined.
    #- `min_t` is initially undefined.
    #- `sticks` is a list of integers.
    #
    #### Loop Logic
    #The loop iterates over `i` starting from `mid + 1` up to `100` (inclusive).
    #
    #For each iteration:
    #- `cost` is calculated as the sum of the minimum absolute differences between each element `x` in `sticks` and `i` and `i-1`.
    #- If `cost` is less than `min_cost`, `min_cost` is updated to `cost`, and `min_t` is set to the current value of `i`.
    #
    #### Analysis of Iterations
    #Let's analyze the loop based on the provided output states for the first few iterations:
    #
    ##### After 1 iteration
    #- `i` is `mid + 1`.
    #- `cost` is the sum of minimum absolute differences for `sticks` with respect to `i` and `i-1`.
    #- If `cost < min_cost`, `min_cost` is updated to `cost` and `min_t` is set to `mid + 1`.
    #- If `cost >= min_cost`, `min_cost` and `min_t` remain unchanged.
    #
    ##### After 2 iterations
    #- `i` is `mid + 2`.
    #- `cost` is the sum of minimum absolute differences for `sticks` with respect to `i` and `i-1`.
    #- If `cost < min_cost`, `min_cost` is updated to `cost` and `min_t` is set to `mid + 2`.
    #- If `cost >= min_cost`, `min_cost` and `min_t` remain unchanged.
    #
    ##### After 3 iterations
    #- `i` is `mid + 3`.
    #- `cost` is the sum of minimum absolute differences for `sticks` with respect to `i` and `i-1`.
    #- If `cost < min_cost`, `min_cost` is updated to `cost` and `min_t` is set to `mid + 3`.
    #- If `cost >= min_cost`, `min_cost` and `min_t` remain unchanged.
    #
    #From these patterns, we can infer that the loop will continue until `i` reaches `100`, or until `min_cost` cannot be further improved by any subsequent iteration.
    #
    #### Final Output State
    #- The loop will eventually execute for all `i` from `mid + 1` to `100`.
    #- `min_cost` will hold the minimum value of `cost` encountered during the loop.
    #- `min_t` will hold the value of `i` corresponding to the minimum `cost`.
    #
    #Thus, the output state after all iterations of the loop have finished is:
    #
    #**Output State: `i` is `100`, `cost` is the sum of minimum absolute differences for `sticks` with respect to `i` and `i-1`, `min_cost` is the minimum value of `cost` encountered during the loop, and `min_t` is the value of `i` corresponding to `min_cost`.**
    #
    #Note: If the loop does not execute at all (i.e., `mid + 1` is greater than or equal to `100`), then `min_cost` and `min_t` will remain their initial undefined states.
    print(min_t, min_cost)
#Overall this is what the function does:Functionality: **The function `func()` accepts no parameters directly but relies on input from the user. It processes a list of integers `sticks` and determines the integer `t` that minimizes the sum of the minimum absolute differences between each element in `sticks` and either `t` or `t+1`. The function sorts the list `sticks` and initializes `t` and `min_cost` with the median of `sticks`. It then iterates from `mid - 1` down to `1` and from `mid + 1` up to `100`, updating `min_cost` and `min_t` if a lower cost is found. After the loops, the function prints the value of `min_t` and `min_cost`.

Potential edge cases include:
- If the input list `sticks` has fewer than 2 elements, the function will raise an error because the median calculation (`mid = sticks[n // 2]`) will be invalid.
- If the input list `sticks` is empty, the function will also raise an error due to the same reason as above.

Missing functionality:
- The function does not handle the case where the input list `sticks` contains duplicate values. The median calculation and subsequent operations assume unique values in `sticks`.

