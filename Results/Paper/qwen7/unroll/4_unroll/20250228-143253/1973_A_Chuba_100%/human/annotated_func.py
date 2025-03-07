#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: Output State: The output state will consist of a series of lines, each containing either '-1' or a non-negative integer result. The number of lines will be equal to the value of `t`. Each line's content depends on the input provided during each iteration of the loop. If the sum of the three integers in a line is odd, it will print '-1'. Otherwise, it will print the calculated result based on the formula `(v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2`.
#Overall this is what the function does:The function reads a positive integer `t` and then processes `t` test cases. For each test case, it reads three non-negative integers `p_1`, `p_2`, and `p_3` and checks if their sum is odd. If the sum is odd, it prints `-1`. If the sum is even, it calculates a result using the formula `(p_1 + p_2 + p_3 - max(0, p_3 - p_1 - p_2)) // 2` and prints this result. After processing all test cases, the function ends, printing a series of `-1` or calculated results based on the input provided.

