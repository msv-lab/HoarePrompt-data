#State of the program right berfore the function call: v_1 and v_2 are integers (1 ≤ v_1, v_2 ≤ 100), t is an integer (2 ≤ t ≤ 100), and d is an integer (0 ≤ d ≤ 10).
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
        
    #State of the program after the  for loop has been executed: `v_1` is an integer between 1 and 100, `v_2` is an integer between 1 and 100, `t` is an integer value between 2 and 100, `d` is an integer between 0 and 10, `max_speed` is equal to `max_speed - (t - 1) * d` or `min_speed`, `min_speed` is equal to `min_speed + (t - 1) * d`, `max_length` is `max_speed * t`, `min_length` is `min_speed * t`, and if `t` is 1, the loop does not execute, leaving `max_speed` and `min_speed` unchanged, and `max_length` and `min_length` equal to `max_speed * t` and `min_speed * t` respectively.
    print(max_length)
#Overall this is what the function does:The function accepts no parameters and reads two speed values (`v1` and `v2`), a time value (`t`), and a decrease value (`d`) from user input. It calculates the maximum and minimum speeds over time, considering possible adjustments due to `d`, and computes the total potential distances covered at these speeds. Finally, it prints the total maximum distance covered. The function does not handle negative values for `d`, and it does not return any value.

