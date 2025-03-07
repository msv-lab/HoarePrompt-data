#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 5000) representing the length of the string s. The second line contains a string s of length n consisting of characters '+' and '-'. The number of test cases t is between 1 and 1000, inclusive. There are no constraints on the sum of n over all test cases.
def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `n` is a single integer (1 ≤ `n` ≤ 5000) representing the length of the string `s`; `s` is a string of length `n` consisting of characters '+' and '-'; `neg` is the number of '-' characters in the string `s`.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is the length of the string s and neg is the number of '-' characters in the string s)
#Overall this is what the function does:For each test case, the function reads an integer `n` and a string `s` of length `n` consisting of '+' and '-' characters. It then calculates and prints a value based on the number of '-' characters in the string. Specifically, it prints `n - 2 * neg` if `n` is not equal to `neg` (where `neg` is the count of '-' characters), otherwise it prints `n`.

