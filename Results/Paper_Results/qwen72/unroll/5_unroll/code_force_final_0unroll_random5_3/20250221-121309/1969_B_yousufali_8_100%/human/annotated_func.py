#State of the program right berfore the function call: No variables are passed to the function. The function reads a binary string `s` from the standard input and initializes `n` and `ans` to 0.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is the same binary string input by the user, `n` is the number of '1's in the string, `ans` is the sum of `n + 1` for each '0' that follows at least one '1'.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans` calculated as described above.
    #
    #Given the initial state and the calculation, the output will be:
    #
    #Output:
#Overall this is what the function does:The function reads a binary string `s` from the standard input, processes it to calculate a value `ans` based on the number of '1's and '0's in the string, and prints the result. Specifically, `ans` is the sum of `n + 1` for each '0' that follows at least one '1', where `n` is the count of '1's encountered before the '0'. The function does not return any value. After the function concludes, `s` remains the same binary string input by the user, and `ans` is the printed result.

#State of the program right berfore the function call: No variables are passed to the function `func_2()`. The function reads an integer `t` from the standard input, which represents the number of test cases, and `t` satisfies 1 ≤ t ≤ 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: The function `func_1()` is called `t` times, where `t` is the integer input read from the standard input. The value of `t` remains unchanged after the loop execution.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the standard input, where `t` represents the number of test cases and must satisfy 1 ≤ t ≤ 10^4. The function calls `func_1` exactly `t` times. The function does not return any value, and the value of `t` remains unchanged after the loop execution.

