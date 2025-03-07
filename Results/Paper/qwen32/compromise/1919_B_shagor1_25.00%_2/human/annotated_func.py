#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 5000) representing the length of a string s. The string s consists of n characters, each of which is either '+' or '-'. There are no constraints on the sum of n over all test cases.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `n` is an integer (1 ≤ `n` ≤ 5000) representing the length of the string `s`; `s` is a string of length `n` consisting of '+' and '-' characters; `neg` is the count of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: - The output will be `n - 2 * neg` if the string contains both '+' and '-' characters, or if there are more '+' characters than '-' characters.
    #   - The output will be `n` if the string contains only '-' characters.
    #
    #Based on the above analysis, the output of the print statement can be described as follows:
    #
    #Output:
#Overall this is what the function does:The function `func_1` processes each test case by reading an integer `n` and a string `s` of length `n` consisting of '+' and '-' characters. It calculates and prints the result as `n - 2 * neg` if the string contains both '+' and '-' characters, or if there are more '+' characters than '-' characters. If the string contains only '-' characters, it prints `n`.

