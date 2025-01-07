#State of the program right berfore the function call: v_1 and v_2 are integers such that 1 ≤ v_1, v_2 ≤ 100; t is an integer such that 2 ≤ t ≤ 100; d is an integer such that 0 ≤ d ≤ 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: - If `t` is `2`, then `speeds` will remain as `[v_1, v_2]`.
    #- If `t` is greater than `2`, `speeds[1]` to `speeds[t-1]` will be calculated based on the defined loop logic, ensuring `speeds[i]` will be bounded by the values influenced by `v_1`, `v_2`, and the increment `d`.
    #
    #Thus, we can conclude: 
    #- `speeds[0]` is `v_1`
    #- `speeds[-1]` is `v_2`
    #- Each `speeds[i]` for `1 ≤ i < t` will be determined by the formula in the loop, representing a progressively updated speed value that cannot exceed `v_2`.
    #
    #Output State:
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function accepts two integer inputs v1 and v2 representing initial and final speeds, two integers t representing the total time intervals and d representing the speed increment. It calculates a list of speeds for each time interval ensuring that speeds increase by at most d without exceeding v2, and then it computes and prints the total distance covered based on these speeds. The function does not return any value, and edge cases such as when t is 2 are handled, resulting in a total distance that is simply the sum of v1 and v2.

