#State of the program right berfore the function call: The function `func_1` should actually be defined with parameters to match the problem description. The correct function definition should be `def func_1(t, test_cases):`, where `t` is an integer representing the number of test cases, and `test_cases` is a list of tuples, each containing an integer `n` and a string `s` of length `n` consisting of characters "+" and "-". For each test case, `1 <= n <= 5000` and `s` contains only "+" and "-" characters.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `func_1` is defined with parameters `t` and `test_cases`, `n` is an input integer, `s` is an input string, `neg` is the number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is the input integer and neg is the number of '-' characters in the input string s)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `s` from user input. The string `s` consists of characters "+" and "-". The function calculates the number of "-" characters in `s` and prints the result of `n - 2 * neg` if `n` is not equal to `neg`, otherwise it prints `n`. The function does not return any value.

