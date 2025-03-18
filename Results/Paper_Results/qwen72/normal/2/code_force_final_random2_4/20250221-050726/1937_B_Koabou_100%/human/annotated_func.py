#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 2 × 10^5, and a_{11}a_{12}...a_{1n} and a_{21}a_{22}...a_{2n} are binary strings of length n, where each character is either '0' or '1'. The sum of n over all test cases does not exceed 2 × 10^5.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `a` is a list containing two elements where each element is a user input, `_` is 1.
    s = []
    x = 0
    y = 0
    for i in range(n - 1):
        if a[0][i + 1] == '0' and a[1][i] == '1':
            y = i
        
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `a` is a list containing two elements where each element is a user input, `_` is 1, `s` is either an empty list or a concatenated string formed from parts of `a[0]` and `a[1]` based on the conditions in the loop, `x` is the index where the condition `a[0][i + 1] == '1' and a[1][i] == '0'` was met, or `n - 1` if the loop completes without breaking, `y` is the last index where the condition `a[0][i + 1] == '0' and a[1][i] == '1'` was met, or 0 if the condition was never met, `i` is `n - 2` if the loop completes without breaking, or the last value of `i` before the loop broke.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: `t` is either 1 or `x - i + 1`, `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `a` is a list containing two elements where each element is a user input, `_` is 1, `s` is either an empty list or a concatenated string formed from parts of `a[0]` and `a[1]` based on the conditions in the loop, `x` is at least 1, `y` is 0, `i` is `x - 1` if the loop completes without breaking, or the last value of `i` before the loop broke. If the condition `a[1][i:x] == s[i + 1:x + 1]` was met during any iteration, `t` is set to `x - i + 1` and the loop breaks. Otherwise, `t` remains 1.
    print(s, sep='')
    #This is printed: s (where s is the concatenated string formed from parts of a[0] and a[1] based on the conditions in the loop)
    print(t)
    #This is printed: t (where t is 1 if the condition a[1][i:x] == s[i + 1:x + 1] is never met, or x - i + 1 if the condition is met for some i)
#Overall this is what the function does:The function `func_1` processes a series of test cases. For each test case, it reads an integer `n` and two binary strings of length `n`. It then searches for a specific pattern within these strings and constructs a new string `s` based on certain conditions. If a valid pattern is found, it calculates a value `t` based on the positions of the pattern. Finally, it prints the constructed string `s` and the calculated value `t`. The function does not return any values; it only prints the results.

