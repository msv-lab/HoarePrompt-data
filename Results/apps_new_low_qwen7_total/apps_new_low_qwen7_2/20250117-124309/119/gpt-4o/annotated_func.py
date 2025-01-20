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
                #State of the program after the if-else block has been executed: *`t` is the first integer in the input, `s` is the second integer in the input, and `x` is the third integer in the input. `x` is greater than `t`. If `(x - t - 1) % s == 0` and `x != t + 1`, the output is 'YES'. Otherwise, the output is 'NO'.
            #State of the program after the if-else block has been executed: *`t` is the first integer in the input, `s` is the second integer in the input, and `x` is the third integer in the input. `x` is greater than `t`. If the difference between `x` and `t` is divisible by `s`, the output is 'YES'. Otherwise, if `(x - t - 1) % s == 0` and `x != t + 1`, the output is 'YES'. Otherwise, the output is 'NO'.
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`t` is the first integer in the input, `s` is the second integer in the input, and `x` is the third integer in the input (with `x` not equal to `t`). If `x` is greater than `t`, the output is 'YES' under two conditions: when the difference between `x` and `t` is divisible by `s`, or when `(x - t - 1) % s == 0` and `x` is not equal to `t + 1`. If `x` is less than or equal to `t`, the output remains the same as per the else condition where the output is 'NO'.
    #State of the program after the if-else block has been executed: *`t` is the first integer in the input, `s` is the second integer in the input, and `x` is the third integer in the input. If `x` equals `t`, the program does not change the output. Otherwise, if `x` is greater than `t`, the output is 'YES' if the difference between `x` and `t` is divisible by `s`, or if `(x - t - 1) % s == 0` and `x` is not equal to `t + 1`. If `x` is less than or equal to `t`, the output remains 'NO'.
#Overall this is what the function does:The function `func` accepts three non-negative integers `t`, `s`, and `x` as input, where \(0 \leq t, x \leq 10^9\) and \(2 \leq s \leq 10^9\). It then checks the relationship between these integers and prints 'YES' or 'NO' based on specific conditions. Specifically:
- If `x` is equal to `t`, it prints 'YES'.
- If `x` is greater than `t` and the difference between `x` and `t` is divisible by `s`, it prints 'YES'.
- If `x` is greater than `t`, but the difference between `x` and `t` minus one is divisible by `s` and `x` is not equal to `t + 1`, it also prints 'YES'.
- In all other cases, it prints 'NO'.

Potential edge cases include:
- When `x` is exactly `t`, the function correctly prints 'YES'.
- When `x` is greater than `t` and the difference between them is exactly divisible by `s`, the function prints 'YES'.
- When `x` is greater than `t` and the difference minus one is divisible by `s` but `x` is not `t + 1`, the function prints 'YES'.
- For all other cases, including when `x` is less than or equal to `t`, the function prints 'NO'.

There is no return value; instead, the function directly prints 'YES' or 'NO' based on the conditions.

