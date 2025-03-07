#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, p_1, p_2, and p_3 are integers such that 0 <= p_1 <= p_2 <= p_3 <= 30.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: The loop has executed `t` times, and for each iteration, it has printed either `-1` if the sum of `a`, `b`, and `c` is odd, or the minimum of `(a + b + c) // 2` and `a + b` if the sum is even. The values of `t`, `p_1`, `p_2`, and `p_3` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`. It then processes `t` test cases, each consisting of three integers `a`, `b`, and `c` such that `0 <= a <= b <= c <= 30`. For each test case, if the sum of `a`, `b`, and `c` is odd, the function prints `-1`. If the sum is even, the function prints the minimum of `(a + b + c) // 2` and `a + b`. The function does not return any value; it only prints the results for each test case. The values of `t`, `a`, `b`, and `c` are not modified and remain as they were read from the input.

