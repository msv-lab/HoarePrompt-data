#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are positive integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is greater than or equal to 0, `i` is `t - 1`, `a`, `b`, and `m` are input integers. If `m` is less than `a` or less than `b`, the current value of `m` remains less than `a` or less than `b`. Otherwise, `m` is greater than or equal to both `a` and `b`.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads three positive integers `a`, `b`, and `m`. If `m` is less than either `a` or `b`, it prints `2`. Otherwise, it prints the sum of the integer division of `m` by `a`, the integer division of `m` by `b`, and `2`. After processing all test cases, the function completes, and the final state is that `t` is greater than or equal to 0, `i` is `t - 1`, and `a`, `b`, and `m` are the last input integers for the final test case.

