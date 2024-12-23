#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100, t is an integer such that 2 ≤ t ≤ 100, and d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    max_speed = max(v1, v2)
    min_speed = min(v1, v2)
    max_length = max_speed * t
    min_length = min_speed * t
    for i in range(t - 1, 0, -1):
        max_speed = max(max_speed - d, min_speed)
        
        min_speed = min(min_speed + d, max_speed)
        
        max_length += max_speed
        
        min_length += min_speed
        
    #State of the program after the  for loop has been executed: `v1` is an integer such that \(1 \leq v1 \leq 100\); `v2` is an integer such that \(1 \leq v2 \leq 100\); `t` is an integer such that \(2 \leq t \leq 100\); `d` is an integer such that \(0 \leq d \leq 10\); `max_speed` is the maximum of `v1` and `v2` reduced by \(d\) for each iteration until it equals `min_speed`; `min_speed` is the minimum of `v1` and `v2` increased by `d` until it equals `max_speed`; `max_length` is the sum of all `max_speed` values from each iteration; `min_length` is the sum of all `min_speed` values from each iteration; `i` is 0.
    print(max_length)
#Overall this is what the function does:The function `func()` accepts four parameters: `v1` and `v2` (both integers between 1 and 100), `t` (an integer between 2 and 100), and `d` (an integer between 0 and 10). It calculates two lengths, `max_length` and `min_length`, based on the speeds `max_speed` and `min_speed` which start as the maximum and minimum of `v1` and `v2`, respectively. Over the course of `t-1` iterations, `max_speed` decreases by `d` while `min_speed` increases by `d` until they meet. In each iteration, `max_length` and `min_length` are updated accordingly. Finally, the function prints the value of `max_length`.

If `d` is 0, the function simplifies the calculation and directly returns `v1 + v2`. Otherwise, it iterates through the process described above to compute the lengths.

