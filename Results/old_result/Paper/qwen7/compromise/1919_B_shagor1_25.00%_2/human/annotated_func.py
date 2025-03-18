#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-', where the i-th character of s represents a_i = 1 if s_i = '+' and a_i = -1 if s_i = '-'.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer such that 1 ≤ n ≤ 5000, `s` is a string of length `n` consisting of characters '+' and '-', `neg` is the number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where `n` is the input integer and `neg` is the number of '-' characters in the string `s`)
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (1 ≤ t ≤ 1000), an integer `n` (1 ≤ n ≤ 5000), and a string `s` of length `n` containing characters '+' and '-'. For each test case, it calculates and prints the value of `n - 2 * neg`, where `neg` is the count of '-' characters in `s`. If `n` equals `neg`, it prints `n` instead.

