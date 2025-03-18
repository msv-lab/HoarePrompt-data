#State of the program right berfore the function call: The function should actually be defined with parameters to match the problem description. The correct function definition should be `def func_1(s, n):` where `s` is a string of length `n` consisting of characters "+" and "-", and `n` is a positive integer such that 1 <= n <= 5000.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `s` is a string with any number of characters, `neg` is the count of '-' characters in the string `s`, and `func_1(s, n)` is defined with parameters `s` and `n` where `1 <= n <= 5000`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: - Since the exact values of `n` and `neg` are not provided, we can only describe the output based on the given conditions.
    #   - If `n` is not equal to `neg`, the output will be `n - 2 * neg`.
    #   - If `n` is equal to `neg`, the output will be `n`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `s` from the user input. The string `s` is expected to consist of characters "+" and "-", and `n` is the length of `s` with the constraint 1 <= n <= 5000. The function calculates the number of '-' characters in `s` and prints a value based on the following conditions: if the number of '-' characters is not equal to `n`, it prints `n - 2 * neg`; otherwise, it prints `n`. The function does not return any value.

