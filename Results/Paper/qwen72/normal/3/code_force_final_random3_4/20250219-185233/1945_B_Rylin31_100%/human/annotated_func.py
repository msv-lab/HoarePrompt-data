#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `i` is `t-1`, `a`, `b`, and `m` are input integers.
#Overall this is what the function does:The function `func` reads an integer `t` (1 <= t <= 10^4) from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` (1 <= a, b, m <= 10^18) from the input. It then calculates and prints the value of `m // a + m // b + 2` for each test case. After processing all test cases, the function concludes without returning any value. The final state of the program is that `t` test cases have been processed, and the results for each test case have been printed.

