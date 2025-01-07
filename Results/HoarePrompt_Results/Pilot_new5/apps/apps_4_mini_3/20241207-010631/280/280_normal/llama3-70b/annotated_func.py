#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100; t is an integer such that 2 ≤ t ≤ 100; d is an integer such that 0 ≤ d ≤ 10.
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
        
    #State of the program after the  for loop has been executed: `v_1` is an integer between 1 and 100, `v_2` is an integer between 1 and 100, `t` is greater than or equal to 2, `d` is an integer from user input, `max_speed` is the maximum of `max_speed - d * (t - 1)` and `min_speed`, `min_speed` is the minimum of `min_speed + d * (t - 1)` and `max_speed`, `max_length` is `max_speed * t`, `min_length` is `min_speed * t`, `i` is 0.`
    print(max_length)
#Overall this is what the function does:The function accepts two integer inputs `v1` and `v2` representing speeds, an integer `t` representing time, and an integer `d` representing the change in speed. It calculates the maximum and minimum distance covered over the time period `t`, where the maximum speed is reduced by `d` and the minimum speed is increased by `d` in each iteration of a loop. The function outputs the maximum distance covered and does not return any value. Edge cases include ensuring that the speeds do not go below the minimum or above the maximum during the adjustments. The function lacks error handling for invalid input types and assumes valid inputs are provided within the specified ranges.

