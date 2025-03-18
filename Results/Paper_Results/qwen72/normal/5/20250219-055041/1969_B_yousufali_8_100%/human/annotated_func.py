#State of the program right berfore the function call: s is a binary string (a string consisting of only '0' and '1' characters) with a length of at least 2.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is a new binary string input by the user, with a length of at least 2; `i` is `len(s) - 1`; `n` is the number of '1's in `s`; `ans` is the sum of `n + 1` for each '0' in `s` that follows at least one '1'.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans` calculated as described above.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads a binary string `s` from user input, where `s` consists of '0' and '1' characters and has a length of at least 2. It calculates a value `ans` based on the number of '1's (`n`) in the string and the positions of '0's that follow at least one '1'. Specifically, for each '0' that follows at least one '1', `ans` is incremented by `n + 1`. The function then prints the final value of `ans` and does not return any value.

#State of the program right berfore the function call: No variables are passed to the function `func_2()`. The function reads an integer `t` from the standard input, where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, `func_1()` is called.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` must be greater than or equal to the number of iterations, `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the standard input, where `1 ≤ t ≤ 10^4`, and calls the function `func_1` exactly `t` times. The function does not return any value, and after its execution, `t` will be greater than or equal to the number of times `func_1` has been called.

