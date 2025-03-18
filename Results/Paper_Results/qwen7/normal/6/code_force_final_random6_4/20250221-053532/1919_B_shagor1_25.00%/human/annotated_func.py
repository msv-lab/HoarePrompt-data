#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string consisting of '+' and '-' characters with length n.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 5000, `s` is a string consisting of '+' and '-' characters with length `n`, `i` is equal to `n`, and `neg` is the total count of '-' characters in the string `s`.
    #
    #Explanation: After all the iterations of the loop, the variable `i` will be equal to the length of the string `s`, which is `n`. The variable `neg` will hold the total count of '-' characters encountered in the string `s` during the loop execution. The variables `t` and `n` remain unchanged as they are not affected by the loop.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is the length of the string s and neg is the count of '-' characters in the string s)
#Overall this is what the function does:The function processes a string `s` containing '+' and '-' characters. It counts the number of '-' characters in the string and calculates a result based on the length of the string and the count of '-' characters. Specifically, it returns the length of the string minus twice the count of '-' characters, unless the count of '-' characters equals the length of the string, in which case it returns the length of the string.

