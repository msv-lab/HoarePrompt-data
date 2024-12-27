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
        
    #State of the program after the  for loop has been executed: `max_speed` is the final maximum speed after adjustments, `min_speed` is the final minimum speed after adjustments, `max_length` is the cumulative maximum distance, `min_length` is the cumulative minimum distance, with `t` determining the number of iterations and `d` influencing the speed adjustments. If `t` is 0 or negative, the loop does not execute, and the variables retain their initial values based on `v1`, `v2`, and `t`.
    print(max_length)
#Overall this is what the function does:The function accepts no explicit parameters but reads four integer values from the user: two speeds (`v1` and `v2`) and two integers (`t` and `d`). It calculates the maximum and minimum speeds, then iteratively adjusts these speeds based on the given decrement (`d`) for `t-1` iterations, keeping the adjusted speeds within the bounds of each other. After the loop, it calculates the cumulative maximum distance (`max_length`) and prints this value. The state of the program after execution includes the final maximum speed, minimum speed, cumulative maximum distance, and cumulative minimum distance, with `t` determining the number of iterations and `d` influencing the speed adjustments. The function does not handle cases where `t` is less than 2 or `d` is outside the range of 0 to 10, and it assumes that `v1` and `v2` will always be positive integers between 1 and 100. The output is the cumulative maximum distance after the speed adjustments.

