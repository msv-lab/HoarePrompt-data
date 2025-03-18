#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string consisting of '+' and '-' characters with length n.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer such that 1 ≤ n ≤ 5000, `s` is a string consisting of '+' and '-' characters with length n, `neg` is the number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is the input integer and neg is the number of '-' characters in the string s)
#Overall this is what the function does:The function processes an input string `s` consisting of '+' and '-' characters and calculates a result based on the count of '-' characters in the string. Specifically, it prints `n - 2 * neg` if `n` is not equal to `neg`, otherwise it prints `n`, where `n` is the length of the string `s` and `neg` is the number of '-' characters in `s`. The function implicitly handles multiple test cases, each defined by an integer `t`, an integer `n`, and a string `s`. After processing each test case, it outputs the calculated result.

