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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer where 2 ≤ `t` ≤ 100; `d` is a non-negative integer where 0 ≤ `d` ≤ 10; `v1` and `v2` are unchanged; `max_speed` is the final value after the loop; `min_speed` is the final value after the loop; `max_length` is equal to the total increment of `max_speed` over `t-1` iterations; `min_length` is equal to the total increment of `min_speed` over `t-1` iterations.
    print(max_length)
#Overall this is what the function does:The function reads four integers from user input: v1, v2 (speeds), t (time), and d (speed variation). It calculates the maximum and minimum possible distances traveled over the time period t based on the given speed variations. Specifically, it iterates through the time decrementing the maximum speed by d (until it reaches the minimum speed) and incrementing the minimum speed by d (until it reaches the current maximum speed). After performing these calculations, it sums the adjusted maximum and minimum speeds to compute the total maximum distance traveled. The function then prints the final total maximum distance calculated. Notably, the function does not directly take parameters and has no explicit return value; the result is printed instead. Additionally, while the function manages speeds and distances, it does not handle potential invalid user inputs (e.g., ensuring inputs comply with stated constraints).

