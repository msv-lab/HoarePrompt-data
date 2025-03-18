#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18) where a and b represent the frequency of launching fireworks for the first and second installations, respectively, and m represents the duration for which each firework is visible in the sky. There are t (1 ≤ t ≤ 10^4) test cases.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has executed `t` times, and for each iteration, the output is either `2` if `m` is less than `a` or `m` is less than `b`, or `m // a + m // b + 2` if `m` is greater than or equal to both `a` and `b`. The values of `a`, `b`, `m`, and `t` remain unchanged throughout all iterations, and `i` has been incremented from `0` to `t-1`.
#Overall this is what the function does:The function reads `t` test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints a value: `2` if `m` is less than either `a` or `b`, or `m // a + m // b + 2` if `m` is greater than or equal to both `a` and `b`.

