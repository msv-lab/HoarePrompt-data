#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers where 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The values of `t`, `a`, `b`, and `m` remain unchanged, but the loop will have printed `t` lines, each containing the result of the expression `m // a + m // b + 2` for the corresponding input values of `a`, `b`, and `m`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 ≤ t ≤ 10^4`, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input, where `1 ≤ a, b, m ≤ 10^18`. The function then calculates the expression `m // a + m // b + 2` for each test case and prints the result. After processing all `t` test cases, the function completes, and the values of `t`, `a`, `b`, and `m` are not retained. The function does not return any value.

