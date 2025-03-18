#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, p_1, p_2, and p_3 are integers such that 0 <= p_1 <= p_2 <= p_3 <= 30.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The loop executes `t` times, and for each iteration, it reads three integers from the input, checks if their sum is odd, and if so, prints `-1`. If the sum is even, it calculates a result based on the formula provided and prints the result. The values of `p_1`, `p_2`, and `p_3` are not affected by the loop and remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`, and then for each of the `t` test cases, it reads three integers `p_1`, `p_2`, and `p_3` (where `0 <= p_1 <= p_2 <= p_3 <= 30`). For each test case, if the sum of `p_1`, `p_2`, and `p_3` is odd, it prints `-1`. If the sum is even, it calculates a result using the formula `(p_1 + p_2 + p_3 - max(0, p_3 - p_1 - p_2)) // 2` and prints this result. The function does not return any value; it only prints the results to the console. The values of `p_1`, `p_2`, and `p_3` are not modified by the function.

