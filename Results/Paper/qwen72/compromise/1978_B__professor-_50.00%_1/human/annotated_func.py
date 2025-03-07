#State of the program right berfore the function call: The function should take three parameters: n, a, and b, where n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: The values of `n`, `a`, and `b` are not retained after each iteration of the loop, and the loop runs `t` times, printing a result for each set of inputs. The variables `n`, `a`, and `b` are re-assigned in each iteration based on the input, and their final values after the loop are the values from the last iteration. The variable `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the user, indicating the number of test cases. For each of the `t` test cases, it reads three integers `n`, `a`, and `b` from the user. Based on the values of `a` and `b`, it calculates and prints a result for each test case. The final state of the program after the function concludes is that `t` test cases have been processed, and a result has been printed for each. The variables `n`, `a`, and `b` are re-assigned in each iteration and their final values are those from the last test case. The variable `t` remains unchanged.

