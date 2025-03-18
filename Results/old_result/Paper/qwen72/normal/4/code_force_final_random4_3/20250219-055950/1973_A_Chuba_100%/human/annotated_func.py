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
        
    #State: `t` is an input integer such that 1 <= t <= 500, `_` is `t-1`, `v` is a list of integers provided by the user. For each iteration, if the sum of the first three elements of `v` (i.e., `v[0] + v[1] + v[2]`) is odd, `-1` is printed. If the sum is even, `result` is set to `(v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2` and this value is printed.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, where `1 <= t <= 500`, indicating the number of test cases. For each test case, it reads three integers `p_1`, `p_2`, and `p_3` (where `0 <= p_1 <= p_2 <= p_3 <= 30`) from the user. If the sum of these three integers is odd, the function prints `-1`. If the sum is even, it calculates a result using the formula `(p_1 + p_2 + p_3 - max(0, p_3 - p_1 - p_2)) // 2` and prints this result. After processing all `t` test cases, the function concludes.

