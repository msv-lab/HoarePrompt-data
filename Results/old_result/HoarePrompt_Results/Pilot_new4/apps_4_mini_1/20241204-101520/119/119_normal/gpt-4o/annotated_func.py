#State of the program right berfore the function call: t, s, and x are non-negative integers where 0 ≤ t, x ≤ 10^9 and 2 ≤ s ≤ 10^9.
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
                #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are non-negative integers where 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9. If `(x - t - 1) % s == 0` and `x` is not equal to `t + 1`, the output is 'YES'. Otherwise, if either `(x - t - 1) % s != 0` or `x` is equal to `t + 1`, the output is 'NO'.
            #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are non-negative integers where 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9; additionally, `x` is not equal to `t`, `x` is greater than `t`. If `(x - t) % s == 0`, the output is 'YES'. Otherwise, if `(x - t - 1) % s == 0` and `x` is not equal to `t + 1`, the output is 'YES'; otherwise, the output is 'NO'.
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are non-negative integers where 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9; additionally, `x` is not equal to `t`. If `x` is greater than `t`, the output will be 'YES' if either `(x - t) % s == 0` or `(x - t - 1) % s == 0` (provided `x` is not equal to `t + 1`); otherwise, the output will be 'NO'. If `x` is less than or equal to `t`, the output will be 'NO'.
    #State of the program after the if-else block has been executed: *`t`, `s`, and `x` are non-negative integers where 0 ≤ `t`, `x` ≤ 10^9 and 2 ≤ `s` ≤ 10^9. If `x` is equal to `t`, the output is 'YES'. If `x` is greater than `t`, the output will be 'YES' if either `(x - t) % s == 0` or `(x - t - 1) % s == 0` (provided `x` is not equal to `t + 1`); otherwise, the output will be 'NO'. If `x` is less than or equal to `t`, the output will be 'NO'.
#Overall this is what the function does:The function reads three non-negative integers `t`, `s`, and `x` from input. It returns 'YES' if `x` is equal to `t`, or if `x` is greater than `t` and either `(x - t) % s == 0` or `(x - t - 1) % s == 0` (provided `x` is not equal to `t + 1`). In all other cases, it returns 'NO'. If `x` is less than or equal to `t`, the function also returns 'NO'.

