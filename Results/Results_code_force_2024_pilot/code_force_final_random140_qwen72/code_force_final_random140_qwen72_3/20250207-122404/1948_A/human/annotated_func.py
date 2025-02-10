#State of the program right berfore the function call: No input parameters are required for the function `func_1`. The function reads an integer `n` from standard input, where 1 ≤ n ≤ 50.
def func_1():
    n = int(input())
    if (n <= 1) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 0
        res = ''
        while n > 0:
            if n >= 2:
                res += letter[i % 26] * 2
                n -= 2
            else:
                res += letter[i % 26]
                n -= 1
            
            i += 1
            
        #State: `n` is 0, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `i` is `initial_n // 2`, and `res` is a string where each pair of consecutive letters from 'A' to the letter corresponding to `i % 26` is repeated twice, except for the last letter which may appear only once if `initial_n` is odd.
        print(res)
        #This is printed: AA
    #State: *`n` is an integer between 1 and 50 (inclusive). If `n` is 1 or less, the current value of `n` is 1 or less. Otherwise, `n` is greater than 1, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `i` is `initial_n // 2`, and `res` is a string where each pair of consecutive letters from 'A' to the letter corresponding to `i % 26` is repeated twice, except for the last letter which may appear only once if `initial_n` is odd.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `n` from standard input, where 1 ≤ n ≤ 50. If `n` is 1 or less, it prints 'NO'. If `n` is greater than 1, it prints 'YES' followed by a string `res` constructed by repeating pairs of consecutive letters from 'A' to the letter corresponding to `i % 26` (where `i` is incremented starting from 0), with each pair repeated twice, except for the last letter which may appear only once if `n` is odd. After the function concludes, `n` is 0, and the string `res` is printed.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer input by the user within the range 1 to 50, and the loop has completed all `t` iterations. The variable `_` is a placeholder and does not affect the loop's execution.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, ensuring that `1 <= t <= 50`. It then calls the function `func_1` exactly `t` times. After the function completes, `t` remains the integer input by the user, and `func_1` has been executed `t` times. The function does not return any value.

