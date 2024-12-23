#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100, t is an integer such that 2 ≤ t ≤ 100, and d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `v1` is `a`, `v2` is `b`, `t` is a positive integer greater than or equal to 1, `d` is the second integer input, `speeds` is a list of length `t` where the first element is `a` and the last element is `b`, and each element `speeds[i]` for `1 ≤ i < t` is calculated as `min(speeds[i - 1] + d, v2 + (t - i - 1) * d)`.
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function accepts two initial speeds `v_1` and `v_2` (integers within the range [1, 100]), a time duration `t` (an integer within the range [2, 100]), and a speed increment `d` (an integer within the range [0, 10]). It then calculates a list of speeds for each time step from 0 to `t-1`, ensuring that the speeds do not exceed `v_2 + (t - i - 1) * d`. The first speed in the list is set to `v_1`, and the last speed is set to `v_2`. After calculating the speeds, it computes the total distance traveled based on these speeds and prints the result. Potential edge cases include the minimum speed not being updated correctly if `d` is 0, and the maximum speed exceeding `v_2` if `d` is large enough.

