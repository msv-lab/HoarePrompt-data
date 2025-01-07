#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100, t is an integer such that 2 ≤ t ≤ 100, and d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer at least 2, `d` is the second integer entered by the user, `speeds` is a list of `t` elements where for each index `i` from 0 to `t-1`, `speeds[i]` is the minimum value between `speeds[i-1] + d` and `v2 + (t - i - 1) * d`, `v1` is no longer defined, `v2` is no longer defined.
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function reads four integers `v1`, `v2`, `t`, and `d` from the standard input, initializes a list `speeds` based on these values, and prints the total distance traveled, which is the sum of all elements in the `speeds` list.

