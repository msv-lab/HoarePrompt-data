#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 5000) and a string s (s_i ∈ {'+', '-'} and |s| = n) representing the length and content of the string for each test case. However, the provided function definition does not match the problem description. The correct function definition should be:
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: The variable `neg` will be equal to the number of '-' characters in the string `s`, and the value of `s` will remain unchanged.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is the length of the string s and neg is the number of '-' characters in the string s)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `s` from the standard input. It then counts the number of '-' characters in the string `s` and stores this count in the variable `neg`. Finally, it prints `n - 2 * neg` if `n` is not equal to `neg`, otherwise it prints `n`. The function does not accept any parameters and does not return any value.

