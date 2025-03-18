#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5, and for each test case, the grid is a 2 \times n matrix where each element is either 0 or 1.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `a` is a list containing two input values.
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `a` is a list containing two input values, `s` is the concatenated string of `a[0]` and `a[1][n-1]` if no condition `a[0][i + 1] == '1' and a[1][i] == '0'` is met, otherwise `s` is the concatenated string of `a[0][:i + 1]` and `a[1][i:]` where `i` is the first index that meets the condition, `x` is `n-1` if no condition is met, otherwise `x` is the first index `i` that meets the condition.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: `t` is `x - i + 1` where `i` is the first index that meets the condition `a[0][:i + 1] == s[:i + 1]`, or `t` remains 1 if no such condition is met. `n`, `a`, `s`, and `x` remain unchanged.
    print(s, sep='')
    #This is printed: s (where s is the value of the string s)
    print(t)
    #This is printed: t (where t is 1 if no index i meets the condition `a[0][:i + 1] == s[:i + 1]`, or t is `x - i + 1` if the condition is met at the first such index i)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a 2xN grid (represented as two strings of 0s and 1s) from user input. It then processes the grid to find the first column index `i` where the element in the first row is '1' and the element in the second row is '0'. If such an index is found, it constructs a new string `s` by concatenating the substring from the first row up to index `i` with the substring from the second row starting from index `i`. If no such index is found, `s` is constructed by concatenating the entire first row with the last element of the second row. The function also calculates an integer `t` which is the length of the longest prefix of the first row that matches the corresponding prefix of `s`. Finally, the function prints the string `s` and the integer `t`.

