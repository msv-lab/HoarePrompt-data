#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string consisting of '+' and '-' characters with length n.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: After all iterations of the loop, `s` is a string consisting of '+' and '-' characters, `i` is the last character in the string `s`, and `neg` is the total count of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is a variable and neg is the count of '-' characters in the string s)
#Overall this is what the function does:The function processes a string `s` consisting of '+' and '-' characters and calculates and prints either `n - 2 * neg` or `n` based on whether `n` is equal to `neg` (the count of '-' characters in `s`). The function implicitly handles multiple test cases by reading inputs until no more are available.

