#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 2 * 10^5. The sum of n over all test cases does not exceed 2 * 10^5. Each of the two binary strings provided for a test case is of length n and consists only of the characters '0' and '1'.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is the input integer such that 2 <= n <= 2 * 10^5; `a` is a list containing two binary strings, each of length `n` and consisting only of the characters '0' and '1'.
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: t is an integer such that 1 <= t <= 10^4; n is the input integer such that 2 <= n <= 2 * 10^5; a is a list containing two binary strings, each of length n; s is the constructed string based on the loop's logic; x is the index where the condition was met or n-1 if the condition was never met.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: t is 1; n is the input integer such that 2 <= n <= 2 * 10^5; a is a list containing two binary strings, each of length n; s is the constructed string based on the loop's logic; x is n - 1.
    print(s, sep='')
    #This is printed: s (where s is a binary string of length n constructed by comparing corresponding characters from the two binary strings in a)
    print(t)
    #This is printed: 1
#Overall this is what the function does:The function `func_1` reads an integer `n` and two binary strings of length `n`. It constructs a new binary string `s` by finding the first position where the second string has a '1' and the first string has a '0', and then combines parts of the two strings. It also calculates an integer `t` based on the constructed string `s` and the first string. The function prints the constructed string `s` and the integer `t`.

