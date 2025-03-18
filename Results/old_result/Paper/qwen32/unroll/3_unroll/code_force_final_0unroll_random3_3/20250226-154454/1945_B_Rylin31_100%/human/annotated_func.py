#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The output state consists of `t` lines, each containing the result of the expression `m // a + m // b + 2` for the corresponding values of `a`, `b`, and `m` read from the input for each test case. The variables `t`, `a`, `b`, and `m` retain their last assigned values from the input, but the primary output is the series of printed results.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates the value of the expression `m // a + m // b + 2` and prints the result.

