#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100, t is an integer such that 2 ≤ t ≤ 100, and d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())

t, d = map(int, input().split())

speeds = [0] * t

speeds[0] = v1

speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: v1 is an integer (1 ≤ v1 ≤ 100), v2 is an integer (1 ≤ v2 ≤ 100), t is an integer (2 ≤ t ≤ 100), d is an integer (0 ≤ d ≤ 10), speeds is a list of length t where the first element is v1, each subsequent element is calculated as min(speeds[i - 1] + d, v2 + (t - i - 1) * d) up to the second last element, and the last element is v2, i is t-1.
    total_distance = sum(speeds)

print(total_distance)
#Overall this is what the function does:The function reads two sets of integers from the user input: `v1` and `v2` (1 ≤ v1, v2 ≤ 100), and `t` and `d` (2 ≤ t ≤ 100, 0 ≤ d ≤ 10). It initializes a list `speeds` of length `t` with all elements set to 0. The first element of `speeds` is set to `v1`, and the last element is set to `v2`. For each index `i` from 1 to `t-1`, the `i`-th element of `speeds` is updated to the minimum of the previous speed plus `d` or `v2` plus the remaining steps multiplied by `d`. Finally, the function calculates the total distance traveled by summing all elements in the `speeds` list and prints this total distance. The function does not return any value; it only prints the total distance. The function does not handle any edge cases mentioned in the annotations (e.g., "Equal speeds", "Short duration", "Long distance").

