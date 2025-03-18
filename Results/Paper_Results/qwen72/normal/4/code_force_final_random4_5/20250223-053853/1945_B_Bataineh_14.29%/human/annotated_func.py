#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has finished executing, and the output for each test case is either 2 or the value of `m // a + m // b + 2`, depending on the conditions `m < a` or `m < b`. The values of `t`, `a`, `b`, and `m` are not retained after each iteration, as they are re-assigned in each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It then prints either `2` if `m` is less than `a` or `b`, or it prints the value of `m // a + m // b + 2` otherwise. After processing all test cases, the function completes, and no values are retained for `t`, `a`, `b`, or `m`. The function does not return any values.

