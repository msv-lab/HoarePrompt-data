#State of the program right berfore the function call: t, s, and x are non-negative integers such that 0 ≤ t, x ≤ 10^9 and 2 ≤ s ≤ 10^9.
def func():
    t, s, x = map(int, input().split())
    if (x == t) :
        print('YES')
    else :
        if (x > t) :
            if ((x - t) % s == 0) :
                print('YES')
            else :
                if ((x - t - 1) % s == 0 and x != t + 1) :
                    print('YES')
                else :
                    print('NO')
                #State of the program after the if-else block has been executed: *`x` is `c`, `t` is `a`, `s` is `b`. If \((x - t - 1) \% s == 0\) and \(x \neq t + 1\), then certain conditions are met. Otherwise, \((x - t - 1) \% s \neq 0\) or \(x = t + 1\).
            #State of the program after the if-else block has been executed: `x` is `c`, `t` is `a`, `s` is `b`. If \((x - t) \% s == 0\), the function prints "YES". Otherwise, the function checks if \((x - t - 1) \% s == 0\) and \(x \neq t + 1\). If these conditions are met, certain conditions are satisfied; otherwise, \((x - t - 1) \% s \neq 0\) or \(x = t + 1\).
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`t` is `a`, `s` is `b`, `x` is `c`, and \(0 \leq t, x \leq 10^9\) and \(2 \leq s \leq 10^9\) are still true. If \(x > t\), the function prints "YES" if \((x - t) \% s == 0\); it checks if \((x - t - 1) \% s == 0\) and \(x \neq t + 1\). If these conditions are met, certain conditions are satisfied; otherwise, \((x - t - 1) \% s \neq 0\) or \(x = t + 1\). If \(x \leq t\), the conditions from the precondition are preserved and the function does nothing additional regarding the print statement.
    #State of the program after the if-else block has been executed: *`t` is `a`, `s` is `b`, `x` is `c`, and \(0 \leq t, x \leq 10^9\) and \(2 \leq s \leq 10^9\) are still true. If \(x > t\), the function prints "YES" if \((x - t) \% s == 0\). If \(x > t\) and \((x - t) \% s \neq 0\) or \(x = t + 1\), the function prints nothing. If \(x \leq t\), the function does nothing additional regarding the print statement.
#Overall this is what the function does:The function takes three non-negative integers \(t\), \(s\), and \(x\) as input, where \(0 \leq t, x \leq 10^9\) and \(2 \leq s \leq 10^9\). It checks if \(x\) can be expressed as \(t + k \cdot s\) for some integer \(k\), considering two special cases when \(x = t + 1\). If \(x = t\), the function prints "YES". If \(x > t\) and \((x - t) \% s == 0\), the function also prints "YES". If \(x > t\) and \((x - t) \% s \neq 0\) or \(x = t + 1\), the function prints "NO". If \(x \leq t\), the function prints "NO". The function does not return a value but prints one of "YES" or "NO" based on the conditions checked.

