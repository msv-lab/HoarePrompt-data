#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 <= v_1, v_2 <= 100, t is an integer such that 2 <= t <= 100, and d is an integer such that 0 <= d <= 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `v1` is the original input integer, `v2` is the original input integer, `t` is the original input integer, `d` is the original input integer, `speeds` is a list where the first element is `v1`, each subsequent element (except the last) is the minimum of the previous element plus `d` and `v2` plus `d` times the number of elements remaining after the current index, the last element is `v2`, and `i` is `t-1` if `t` is greater than 1, otherwise `i` remains undefined because the loop does not execute.
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function reads two initial and final speeds, time, and acceleration, calculates a list of speeds based on these inputs where each subsequent speed is the minimum of the previous speed plus acceleration and the final speed plus acceleration times the remaining time, and prints the total distance traveled by summing up these speeds.

