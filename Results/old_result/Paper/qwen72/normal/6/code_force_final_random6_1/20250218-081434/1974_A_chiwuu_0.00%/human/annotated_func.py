#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x and y are integers such that 0 <= x, y <= 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b * 2
        
        if t % 5 == 0:
            t = t // 5
        else:
            t = t // 5 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `x` and `y` are integers such that 0 <= x, y <= 99, `n` is the input integer, `i` is `n - 1`, `a` is the integer value of the last input string, `b` is the integer value of the second last input string, and `t1` is equal to `t * 15 - b * 4`. If `t1` is greater than or equal to `a`, then `t` remains unchanged. Otherwise, `t` is updated based on the condition `t2 % 15 == 0`: if `t2 % 15 == 0`, `t` is updated to `t + (a - t1) // 15`; otherwise, `t` is updated to `t + (a - t1) // 15 + 1`.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input. It then calculates a value `t` based on `b` and updates `t` based on the relationship between `a` and a derived value `t1`. Finally, it prints the updated value of `t` for each test case. The function does not return any value. After the function concludes, `n` test cases have been processed, and `t` has been printed for each case. The final state of the program includes the processed values of `t` for each test case, but the variables `a`, `b`, `t`, `t1`, and `i` are not retained for use outside the function.

