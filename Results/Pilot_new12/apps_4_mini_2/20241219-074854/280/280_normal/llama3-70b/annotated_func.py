#State of the program right berfore the function call: v_1 and v_2 are integers in the range 1 to 100, t is an integer in the range 2 to 100, and d is an integer in the range 0 to 10.
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
        
    #State of the program after the  for loop has been executed: `v_1` is an input integer between 1 and 100, `v_2` is an input integer between 1 and 100, `t` is greater than or equal to 2, `d` is an input integer, `max_speed` is updated to `max(v_1, v_2) - (t - 1) * d`, `min_speed` is updated to `min(v_1, v_2) + (t - 1) * d`, `max_length` is equal to the cumulative sum over `t - 1` iterations, `min_length` is equal to the cumulative sum over `t - 1` iterations.`
    print(max_length)
#Overall this is what the function does:The function reads two integers (v1 and v2) representing speeds and two integers (t and d) representing time and speed change, respectively. It computes the maximum and minimum cumulative distances covered over a given time `t`, while adjusting the speeds based on the value of `d`. The function iterates from `t-1` down to 1, updating the maximum speed by decreasing it by `d` and the minimum speed by increasing it by `d`, ensuring that the maximum does not go below the minimum speed. After executing the loop, it prints the final computed maximum distance.

