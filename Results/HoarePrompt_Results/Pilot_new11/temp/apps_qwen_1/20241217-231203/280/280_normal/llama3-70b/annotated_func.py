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
        
    #State of the program after the  for loop has been executed: `v1` is an integer between 1 and 100, `v2` is an integer between 1 and 100, `t` is at least 2, `d` is an integer between 0 and 10, `max_speed` is the maximum of `v1` and `v2 - (t-1) * d` if `v1` and `v2 - (t-1) * d` is greater than or equal to the minimum of `v1` and `v2`, else `max_speed` is the minimum of `v1` and `v2`, `min_speed` is the minimum of `min_speed + (t-1) * d` and `max_speed`, `min_length` is `(t + (t-1)) * min_speed`, `max_length` is incremented by `max_speed` exactly `t-1` times.
    print(max_length)
#Overall this is what the function does:The function accepts four parameters: `v1` and `v2` (both integers between 1 and 100), `t` (an integer between 2 and 100), and `d` (an integer between 0 and 10). It calculates and prints the maximum possible distance (`max_length`) a car can travel under certain conditions. Specifically, the function updates `max_speed` and `min_speed` iteratively over `t-1` steps, where `max_speed` and `min_speed` start as the maximum and minimum of `v1` and `v2`, respectively. At each step, `max_speed` decreases by `d` and `min_speed` increases by `d`, ensuring `max_speed` is never less than `min_speed`. After the loop, the function prints `max_length`, which is the sum of `max_speed` values over `t` steps. If `d` is 0, the function sets `max_length` to `v1` and prints it. The function handles the case when `d` is 0 by directly setting `max_length` to `v1`, as no speed changes occur in this scenario.

