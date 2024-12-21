#State of the program right berfore the function call: v_1 and v_2 are integers in the range 1 to 100, t is an integer in the range 2 to 100, and d is an integer in the range 0 to 10.
def func():
    v1, v2 = map(int, input().split())
    t, d = map(int, input().split())
    speeds = [0] * t
    speeds[0] = v1
    speeds[-1] = v2
    for i in range(1, t):
        speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
        
    #State of the program after the  for loop has been executed: `v_1` is in the range 1 to 100; `v_2` is in the range 1 to 100; `t` is greater than or equal to 2; `d` is in the range 0 to 10; `speeds[1]` is equal to `min(v_1 + d, v_2 + (t - 2) * d); speeds[2]` is equal to `min(speeds[1] + d, v_2 + (t - 3) * d); ...; speeds[t-1]` is equal to `min(speeds[t-2] + d, v_2 + 0 * d);` and `i` is `t-1`.
    total_distance = sum(speeds)
    print(total_distance)
#Overall this is what the function does:The function accepts four integer inputs: v1 and v2 (both representing speeds initialized with values between 1 and 100), t (the number of time intervals, with a minimum value of 2), and d (the maximum increment in speed, ranging from 0 to 10). It calculates a list of speeds over t time intervals, starting from v1 and ending at v2, while ensuring that the speed at each intermediate time doesn't exceed the previously calculated speed plus d or the maximum speed that could be achieved based on remaining time intervals. After computing these speeds, the function sums all the speeds in the list and prints the total distance covered as a result. Edge cases include handling the upper limits of speed increments, where the speed may either plateau or not increase if d is zero, and ensuring the starting and ending speeds are adhered to. The final state of the program after execution is the output of the total distance calculated from the speeds array.

