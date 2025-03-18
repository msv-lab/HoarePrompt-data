#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 5000) representing the length of the string s. The following line contains the string s of length n, consisting only of the characters "+" and "-". The number of test cases t is between 1 and 1000, inclusive. There are no constraints on the sum of n over all test cases.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `neg` is the count of '-' characters in the string `s`, `n` is the length of the string `s`, and `s` is the initial string.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is the length of the string s and neg is the count of '-' characters in the string s)
#Overall this is what the function does:The function `func_1` processes multiple test cases, where each test case consists of an integer `n` and a string `s` of length `n` containing only "+" and "-". For each test case, it calculates and prints a value based on the length of the string and the count of "-" characters in it. Specifically, it prints `n - 2 * neg` if `n` is not equal to `neg` (where `neg` is the count of "-" characters), otherwise it prints `n`.

