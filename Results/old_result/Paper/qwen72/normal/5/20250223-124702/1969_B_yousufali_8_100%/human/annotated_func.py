#State of the program right berfore the function call: No variables are passed to the function `func_1`. The function reads a binary string `s` from the standard input, where `s` consists of characters '0' and '1' and has a length of at least 2. The variables `n` and `ans` are initialized to 0 within the function.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `n` is the number of '1's in the string `s`, and `ans` is the sum of `n + 1` for each '0' in `s` that is followed by at least one '1'.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans` as calculated above.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads a binary string `s` from the standard input, where `s` consists of characters '0' and '1' and has a length of at least 2. It then processes the string to calculate a value `ans`, which is the sum of `n + 1` for each '0' in `s` that is followed by at least one '1', where `n` is the number of '1's encountered before the '0'. Finally, the function prints the value of `ans` and does not return any value.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: No variables are passed to the function `func_2`, `t` is an input integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the function `func_1` `t` times. The function does not return any value. After the function concludes, the variable `t` will hold the integer value that was input by the user, and `func_1` will have been called `t` times.

