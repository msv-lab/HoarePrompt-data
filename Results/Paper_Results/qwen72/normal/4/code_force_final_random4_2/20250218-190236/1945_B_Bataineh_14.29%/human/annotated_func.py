#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is greater than 0, `i` is `t-1`, and for each test case, `a`, `b`, and `m` are input integers. If `m` is less than `a` or less than `b`, the condition `m < a or m < b` holds. Otherwise, `m` is greater than or equal to both `a` and `b`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input. If `m` is less than either `a` or `b`, the function prints `2`. Otherwise, it prints the result of `m // a + m // b + 2`. The function does not return any value; it only prints the results to the console. After the function concludes, `t` test cases have been processed, and the corresponding results have been printed.

