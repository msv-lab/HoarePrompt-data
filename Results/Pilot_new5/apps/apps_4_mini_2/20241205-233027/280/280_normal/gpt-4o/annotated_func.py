#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100; t is an integer such that 2 ≤ t ≤ 100; d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `v1` is an input integer (1 ≤ `v1` ≤ 100), `v2` is an input integer (1 ≤ `v2` ≤ 100), `t` is an integer (t ≥ 2), `d` is an integer updated from input, `speeds` is a list of length `t` where `speeds[0]` is equal to `v1`, `speeds[1]` is equal to min(v1 + d, v2 + (t - 2) * d), `speeds[2]` is equal to min(speeds[1] + d, v2 + (t - 3) * d), ..., `speeds[t - 2]` is equal to min(speeds[t - 3] + d, v2 + (t - 4) * d), and `speeds[-1]` is equal to `v2.`
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function accepts input values for two initial speeds `v1` and `v2`, a time period `t`, and a rate of increase `d`. It calculates a list of speeds over `t` time intervals, where the first speed is `v1`, the last speed is `v2`, and each intermediate speed is constrained by the previous speed plus `d` and a maximum that accounts for the remaining time intervals. Finally, the function computes and prints the total distance traveled based on the calculated speeds. It does not directly accept parameters but relies on user input.

