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
        
    #State of the program after the  for loop has been executed: `v1` is an integer input, `v2` is an integer input, `t` is an integer such that \(2 \leq t \leq 100\), `d` is an integer such that \(0 \leq d \leq 10\), `max_speed` is the maximum speed reached after the loop, `min_speed` is the minimum speed reached after the loop, `min_length` is the final value of `min_length` after the loop, `max_length` is the final value of `max_length` after the loop, `i` is 0.
    print(max_length)
#Overall this is what the function does:The function accepts four parameters: `v_1` and `v_2` (both integers within the range [1, 100]), `t` (an integer within the range [2, 100]), and `d` (an integer within the range [0, 10]). It calculates the maximum and minimum speeds over a period of `t` units of time, where each unit of time `i` (from `t-1` down to 0) adjusts these speeds based on the decrement and increment by `d`. The function then prints the final maximum length traveled over the given time period.

