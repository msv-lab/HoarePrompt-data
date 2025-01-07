#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100, t is an integer such that 2 ≤ t ≤ 100, and d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `speeds[0]` is `v1`, `speeds[-1]` is `v2`, and for \(1 \leq i \leq a-2\), `speeds[i]` is the minimum of `speeds[i - 1] + d` and `v2 + (t - i - 1) * d`
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function `func` accepts four parameters: `v_1`, `v_2`, `t`, and `d`, where `v_1` and `v_2` are integers between 1 and 100, `t` is an integer between 2 and 100, and `d` is an integer between 0 and 10. It calculates the total distance traveled over `t` time units given initial speed `v_1`, final speed `v_2`, and a constant acceleration `d`. For each time unit from 1 to `t-1`, the speed is determined as the minimum of either the previous speed plus `d` or a linearly decreasing value starting from `v_2` and decreasing by `d` per unit time. Finally, it prints the total distance traveled.

