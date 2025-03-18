#State of the program right berfore the function call: The function should actually be defined with parameters `n` and `m` as integers where 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers where 1 ≤ n, m ≤ 100, and they are assigned the values from the input. If `(n - m) % 2 == 0` and `n - m >= 0`, the difference `n - m` is a non-negative even number. Otherwise, either `(n - m) % 2 != 0` or `n - m < 0`.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from user input, where both integers are within the range 1 to 100. It then checks if the difference `n - m` is a non-negative even number. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value. After the function concludes, `n` and `m` retain the values read from the input, and the program state reflects the result of the condition check as either 'Yes' or 'No' being printed.

