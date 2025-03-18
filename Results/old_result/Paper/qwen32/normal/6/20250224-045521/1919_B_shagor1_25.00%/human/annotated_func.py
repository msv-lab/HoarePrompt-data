#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 5000) representing the length of the string s. The next line contains a string s of length n consisting of characters '+' and '-'. The number of test cases t is between 1 and 1000, inclusive. There are no constraints on the sum of n over all test cases.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `neg` is equal to the number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where `n` is a given integer and `neg` is the number of '-' characters in the string `s`)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string `s` of length `n` containing only '+' and '-' characters. For each test case, it calculates and prints a value derived from the string `s`, specifically `n - 2 * neg` if `n` is not equal to `neg` (where `neg` is the count of '-' characters in `s`), otherwise it prints `n`.

