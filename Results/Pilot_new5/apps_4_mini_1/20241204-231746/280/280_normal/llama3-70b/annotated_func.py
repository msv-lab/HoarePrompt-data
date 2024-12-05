#State of the program right berfore the function call: v_1 and v_2 are integers representing speeds in meters per second, with 1 ≤ v_1, v_2 ≤ 100; t is an integer representing time in seconds, with 2 ≤ t ≤ 100; d is a non-negative integer representing the maximum speed change per second, with 0 ≤ d ≤ 10.
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
        
    #State of the program after the  for loop has been executed: `v_1` is an integer, `v_2` is an integer, `t` must be at least 2, `d` is an integer, `max_speed` is equal to `max(max_speed - d * (t - 1), min_speed)`, `min_speed` is equal to `min(min_speed + d * (t - 1), max_speed)`, `max_length` is equal to its original value plus `(t - 1) * max_speed`, and `min_length` is equal to its original value plus `(t - 1) * min_speed`.
    print(max_length)
#Overall this is what the function does:The function takes initial speeds `v1` and `v2`, time `t`, and maximum speed change `d`, calculates the maximum distance that can be traveled over `t` seconds given the speed constraints, and prints the maximum distance without returning it.

