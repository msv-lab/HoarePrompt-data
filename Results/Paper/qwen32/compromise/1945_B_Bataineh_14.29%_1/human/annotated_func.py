#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, a, b, and m are positive integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: The output state consists of `t` lines, each being the result of `print(2)` if `m < a` or `m < b` for that iteration, or `print(m // a + m // b + 2)` otherwise. The values of `a`, `b`, and `m` after the loop are those from the last iteration.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three positive integers `a`, `b`, and `m`. For each test case, it prints `2` if `m` is less than either `a` or `b`. Otherwise, it prints the result of the expression `m // a + m // b + 2`.

