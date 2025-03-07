#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-'.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer such that 1 ≤ n ≤ 5000, and `s` is a string of length `n` consisting of characters '+' and '-', `neg` is the number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg (where n is the input integer and neg is the number of '-' characters in the string s)
#Overall this is what the function does:The function processes a single test case consisting of an integer `n` and a string `s` of length `n` containing only '+' and '-' characters. It counts the number of '-' characters in the string and calculates the result based on the formula `n - 2 * neg`, where `neg` is the count of '-' characters. If `n` equals `neg`, it returns `n`; otherwise, it returns `n - 2 * neg`.

