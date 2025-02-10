#State of the program right berfore the function call: No input parameters are required for this function. The function reads an integer n from the standard input, where 1 <= n <= 50.
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
            
        #State: `n` is 0, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `i` is the smallest integer such that `i` = `initial_n` / 2 (rounded up), `res` is a string where each character from 'A' onwards is repeated twice until the total length of the string equals `initial_n`, with the last character possibly being repeated once if `initial_n` is odd.
        print(res)
        #This is printed: (an empty string)
    #State: *No input parameters are required for this function. The variable `n` is an integer read from the standard input, where 1 <= n <= 50. If `n` is 1 or less, no further changes are made. Otherwise, `n` is greater than 1, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `i` is the smallest integer such that `i` = `initial_n` / 2 (rounded up), and `res` is a string where each character from 'A' onwards is repeated twice until the total length of the string equals `initial_n`, with the last character possibly being repeated once if `initial_n` is odd.
#Overall this is what the function does:The function reads an integer `n` from the standard input, where `1 <= n <= 50`. If `n` is 1 or less, it prints "NO" and exits. If `n` is greater than 1, it prints "YES" and constructs a string `res` by repeating each character from 'A' onwards twice until the total length of the string equals `n`, with the last character possibly being repeated once if `n` is odd. Finally, it prints the constructed string `res`.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 50.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is 0 or greater, `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, where `t` is expected to be a positive integer between 1 and 50, inclusive. The function then calls `func_1` exactly `t` times. After the function concludes, `t` remains unchanged, and `func_1` has been executed `t` times. The function does not return any value.

