#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-', where the i-th character represents a_i=1 if s_i= '+' and a_i=-1 if s_i= '-'.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: Postcondition: `i` is the last character in the string `s`, `a` is a list of integers, `x` is an integer, and `neg` is equal to the total number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is the length of the string s and neg is the count of '-' characters in the string s)
#Overall this is what the function does:The function processes a string `s` consisting of '+' and '-' characters. It counts the number of '-' characters in the string and calculates the value of `n - 2 * neg` where `n` is the length of the string and `neg` is the count of '-' characters. If `n` equals `neg`, it returns `n`; otherwise, it returns `n - 2 * neg`. The function prints this calculated value for each test case.

