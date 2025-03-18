#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting only of the characters '+' and '-'.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000; `n` is an input integer such that 1 ≤ n ≤ 5000; `s` is a string of length `n` consisting only of the characters '+' and '-'; `neg` is the count of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if the string s contains any '+' characters, otherwise n (where n is the length of the string s and neg is the count of '-' characters in the string s)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `s` of length `n` consisting of '+' and '-' characters. It calculates and prints the result as `n - 2 * neg` if there are any '+' characters in the string, otherwise it prints `n`, where `neg` is the count of '-' characters in `s`.

