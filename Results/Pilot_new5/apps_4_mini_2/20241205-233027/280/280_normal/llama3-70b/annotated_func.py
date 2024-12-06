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
        
    #State of the program after the  for loop has been executed: `v_1` is an input value (1 ≤ `v_1` ≤ 100), `v_2` is an input value (1 ≤ `v_2` ≤ 100), `t` is an input integer (2 ≤ `t` ≤ 100), `d` is an input integer (0 ≤ `d` ≤ 10), `max_speed` is `max(v_1, v_2) - (t - 1) * d`, `min_speed` is `min(v_1, v_2) + (t - 1) * d`, `max_length` is `max(v_1, v_2) * t + (t - 1) * max(max(v_1, v_2) - d, min(v_1, v_2))`, `min_length` is `min(v_1, v_2) * t + (t - 1) * min(min(v_1, v_2) + d, max(max(v_1, v_2) - d, min(v_1, v_2)))`
    print(max_length)
#Overall this is what the function does:The function accepts input for two integer speeds (`v1` and `v2`), a time duration (`t`), and a change in speed (`d`). It calculates the maximum and minimum lengths traveled over the time period, considering adjustments to the speeds based on `d`, and then prints the maximum length. It does not return any values or handle any invalid input cases.

