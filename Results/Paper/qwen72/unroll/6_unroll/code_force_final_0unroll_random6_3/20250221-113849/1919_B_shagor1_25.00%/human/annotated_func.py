#State of the program right berfore the function call: The function should actually take two parameters: `s` (a string of length n where each character is either '+' or '-') and `n` (an integer such that 1 ≤ n ≤ 5000). Additionally, the function is expected to handle multiple test cases, so the input should include an integer `t` (1 ≤ t ≤ 1000) indicating the number of test cases.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: Output State: `s` is a string of length `n` where each character is either '+' or '-', `n` is an input integer, `t` is an input integer, and `neg` is the number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: - If `n == neg`, the output will be `n`.
    #   - If `n != neg`, the output will be `n - 2 * neg`.
    #
    #Given the initial state, the most precise description of the output is:
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `s` from the user, where `s` is a string of length `n` consisting of '+' and '-' characters. It calculates the number of '-' characters in `s` and prints `n - 2 * neg` if `n` is not equal to `neg`, otherwise it prints `n`. The function does not accept any parameters and does not return any values. It is designed to handle a single test case at a time.

