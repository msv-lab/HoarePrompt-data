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
        
    #State of the program after the  for loop has been executed: `max_length` is the sum of `min_length` and `t * max_speed`, `max_speed` is the maximum of `a` and `b` decreased by `d * (t - 1)`, `min_speed` is the minimum of `a` and `b` increased by `d * (t - 1)`, `min_length` is the sum of `min_speed` multiplied by `t`, `i` is 0 if the loop does not execute, otherwise `i` is 0.
    print(max_length)
#Overall this is what the function does:The function accepts four parameters: `v1` and `v2` (integers between 1 and 100), `t` (an integer between 2 and 100), and `d` (an integer between 0 and 10). It calculates the maximum and minimum speeds based on `v1` and `v2`, and then iteratively updates the maximum and minimum speeds over `t-1` iterations. During each iteration, the maximum length covered is updated based on the current maximum speed, and the minimum length covered is updated based on the current minimum speed. After the loop, the function prints the maximum length covered.

