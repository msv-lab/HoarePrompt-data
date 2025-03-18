#State of the program right berfore the function call: v_1 and v_2 are integers within the range 1 to 100 (inclusive), t is an integer between 2 and 100 (inclusive), and d is an integer between 0 and 10 (inclusive).
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `speeds[i]` for `i` from 1 to `t-1` is updated based on the formula `speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)`, `speeds[0]` is `v_1`, `speeds[t-1]` is `v_2`, `t` is between 2 and 100, `d` is between 0 and 10, `speeds` is a list of length `t`.
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function accepts four integers: `v1` and `v2` (both between 1 and 100 inclusive), `t` (between 2 and 100 inclusive), and `d` (between 0 and 10 inclusive). It computes a list of speeds based on the provided formula, starting with `v1` and ending with `v2`, while ensuring that speeds do not exceed the calculated maximum speed at each step. The function then sums these speeds and prints the total distance traveled. It does not return any value.

