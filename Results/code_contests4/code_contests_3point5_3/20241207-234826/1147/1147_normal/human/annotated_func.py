#State of the program right berfore the function call: **
def func():
    coz = raw_input()
    f, s = raw_input().split()
    d = {'6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
    'A': 14}
    if (f[1] == coz and s[1] != coz) :
        print('YES')
    else :
        if (f[1] != coz and s[1] == coz) :
            print('NO')
        else :
            if (f[1] == s[1] and [f[0]] > d[s[0]]) :
                print('YES')
            else :
                print('NO')
            #State of the program after the if-else block has been executed: *`coz` is a string, `f` and `s` are assigned values based on user input. The second character of `f` is not equal to `coz`, or the second character of `s` is not equal to `coz`, or both conditions are false. If the second character of `f` is equal to the second character of `s`, and the first character of `f` is greater than the value of `d` corresponding to the first character of `s`, then the program executes the if part. Otherwise, if either `f[1]` is not equal to `s[1]` or `f[0]` is less than or equal to `d[s[0]]`, the program executes the else part. In both cases, the program's final state involves the variables `coz`, `f`, and `s` being updated based on the input values, with the program either executing specific conditions or printing 'NO'.
        #State of the program after the if-else block has been executed: *`coz` is a string, `f` and `s` are assigned values based on user input. The second character of `f` is not equal to `coz`, the second character of `s` is equal to `coz`, or both conditions are true. If the second character of `f` is equal to the second character of `s`, and the first character of `f` is greater than the value of `d` corresponding to the first character of `s`, then the program executes the if part and prints 'NO'. Otherwise, if either `f[1]` is not equal to `s[1]` or `f[0]` is less than or equal to `d[s[0]]`, the program executes the else part and prints 'NO'. In both cases, the final state involves the variables `coz`, `f`, and `s` being updated based on the input values, with the program either executing specific conditions or printing 'NO'.
    #State of the program after the if-else block has been executed: *`coz` is a string, `f` and `s` are assigned values based on user input. If the second character of `f` is equal to `coz` and the second character of `s` is not equal to `coz`, the program prints 'YES'. Otherwise, if the second character of `f` is not equal to `coz`, the second character of `s` is equal to `coz`, or both conditions are true, the program checks additional conditions. If the second character of `f` is equal to the second character of `s`, and the first character of `f` is greater than the value of `d` corresponding to the first character of `s`, 'NO' is printed. However, if either `f[1]` is not equal to `s[1]` or `f[0]` is less than or equal to `d[s[0]]`, 'NO' is printed. In both cases, the variables `coz`, `f`, and `s` are updated based on the input values, and the program either prints 'YES' or 'NO' based on the conditions met.
#Overall this is what the function does:The function reads input from the user, assigns values to variables `coz`, `f`, and `s` based on the input, and then prints 'YES' or 'NO' based on specific conditions. If the second character of `f` is equal to `coz` and the second character of `s` is not equal to `coz`, it prints 'YES'. If the second character of `f` is not equal to `coz` and the second character of `s` is equal to `coz`, it prints 'NO'. If the second character of `f` is equal to the second character of `s`, and the first character of `f` is greater than the corresponding value of `d` for the first character of `s`, it prints 'YES'. If none of these conditions are met, it prints 'NO'. The function does not accept any parameters and the output is based solely on user input and the defined conditions.

