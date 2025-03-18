#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100; t is an integer such that 2 ≤ t ≤ 100; d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `v_1` is the first input integer, `v_2` is the second input integer, `t` is the number of elements in `speeds` (which is at least 2), `d` is an integer between 0 and 10, `speeds[0]` is equal to `v_1`, `speeds[1]` to `speeds[t-2]` are calculated values based on previous speeds and the formula used in the loop, `speeds[-1]` is equal to `v_2`.
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function reads four integers from input: `v1` (initial speed), `v2` (final speed), `t` (number of time intervals), and `d` (maximum speed increment). It calculates a list of speeds for each time interval, ensuring that the speed does not exceed the bounds defined by the initial and final speeds nor the increments allowed by `d`. The first speed is set to `v1` and the last to `v2`. Intermediate speeds are computed based on the previous speed and the increment `d`, while ensuring that the speed at any time does not exceed the allowed maximum based on remaining time intervals. Finally, the function computes and prints the total distance traveled, which is the sum of the speeds over the `t` intervals. Note that the function does not return a value but prints the total distance. Potential edge cases include the scenario where `d` is zero, leading to constant speeds throughout the intervals, or where `v1` is equal to `v2`, resulting in all speeds being the same.

