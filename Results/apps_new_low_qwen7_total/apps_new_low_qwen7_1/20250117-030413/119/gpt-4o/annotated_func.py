#State of the program right berfore the function call: t, s, and x are integers such that 0 ≤ t, x ≤ 10^9 and 2 ≤ s ≤ 10^9.
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
                #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are integers such that 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9, with `x` not equal to `t`. If the condition `(x - t - 1) % s == 0 and x != t + 1` holds true, the function prints 'YES'. Otherwise, it prints 'NO'.
            #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are integers such that 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9, with `x` not equal to `t`. If `(x - t) % s == 0` is true, the program prints 'YES'. Otherwise, if `(x - t - 1) % s == 0 and x != t + 1` holds true, the program also prints 'YES'. In all other cases, the program prints 'NO'.
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are integers such that 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9, with `x` not equal to `t`. The program prints 'YES' if either `(x - t) % s == 0` or `(x - t - 1) % s == 0 and x != t + 1` holds true. Otherwise, the program prints 'NO'.
    #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are integers such that 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9. If `x` equals `t`, the console displays 'YES'. Otherwise, the program prints 'YES' if either `(x - t) % s == 0` or `(x - t - 1) % s == 0 and x != t + 1` holds true; otherwise, it prints 'NO'.
#Overall this is what the function does:The function takes no parameters and reads three integers \( t \), \( s \), and \( x \) from standard input, where \( 0 \leq t, x \leq 10^9 \) and \( 2 \leq s \leq 10^9 \). It then checks several conditions to determine whether to print 'YES' or 'NO'. Specifically:

1. If \( x = t \), it prints 'YES'.
2. If \( x > t \):
   - If \( (x - t) \% s == 0 \), it prints 'YES'.
   - If \( (x - t - 1) \% s == 0 \) and \( x \neq t + 1 \), it also prints 'YES'.
   - Otherwise, it prints 'NO'.
3. If \( x < t \), it directly prints 'NO'.

After the function concludes, the state of the program will be such that it has printed either 'YES' or 'NO' based on the conditions evaluated, and the variables \( t \), \( s \), and \( x \) remain unchanged.

