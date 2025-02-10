#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, x and y are integers such that 0 <= x, y <= 9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: `t` must be greater than or equal to the number of iterations, `_` is a placeholder and does not need adjustment, `a` and `b` are the integers entered by the user for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where `1 <= t <= 100`. For each test case, it reads two integers `a` and `b` (both between 0 and 9). It then prints the maximum and minimum of these two integers. After processing all test cases, the function completes, and the state of the program is such that `t` test cases have been processed, and for each test case, the maximum and minimum of the two input integers have been printed.

