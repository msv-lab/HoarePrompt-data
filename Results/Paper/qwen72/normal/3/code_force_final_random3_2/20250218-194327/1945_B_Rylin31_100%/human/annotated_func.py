#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: `t` is an integer provided by user input that must be greater than or equal to the number of iterations, `i` is `t-1`, `a`, `b`, and `m` are integers provided by the latest user input.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from user input. It then calculates and prints the value of `m // a + m // b + 2` for each test case. After processing all test cases, the function completes, and the final state is that `t` test cases have been processed, with `a`, `b`, and `m` being the values from the last test case.

