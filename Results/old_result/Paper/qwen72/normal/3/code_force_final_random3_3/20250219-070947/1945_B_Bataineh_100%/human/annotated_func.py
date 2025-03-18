#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is greater than or equal to the number of iterations, `i` is `t - 1`, and `a`, `b`, and `m` are the input integers provided by the user for the last iteration. If `m` is less than both `a` and `b`, the current value of `m` is less than both `a` and `b`. Otherwise, `m` remains unchanged regardless of its relationship to `a` and `b.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the user. Depending on the values of `a`, `b`, and `m`, it prints a specific integer result for each test case. The function does not return any value, but it prints the result of each test case to the console. After the function concludes, `t` is equal to the number of test cases processed, `i` is `t - 1`, and `a`, `b`, and `m` hold the values of the last test case. The final state of the program is that the function has printed the results for all `t` test cases.

