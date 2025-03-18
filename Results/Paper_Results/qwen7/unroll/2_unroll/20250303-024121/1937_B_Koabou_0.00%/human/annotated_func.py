#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5, and two binary strings a_{11} a_{12} … a_{1n} and a_{21} a_{22} … a_{2n} are given, where each a_{ij} is either 0 or 1. The sum of all n values across all test cases does not exceed 2 \cdot 10^5.
def func_1():
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `a` is a list containing two elements which are the inputs provided during the loop executions; `n` is an input integer.
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `a` is a list containing two elements which are the inputs provided during the loop executions; `n` is an input integer; `s` is a string resulting from the loop's conditions; `x` is an integer indicating the position where the loop modified the string `s`.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: Output State: `t` is 1, `a` is a list containing two elements which are the inputs provided during the loop executions, `n` is an input integer, `s` is a string resulting from the loop's conditions, `x` is an integer indicating the position where the loop modified the string `s`. The value of `t` will be set to `x - i + 1` where `i` is the index when the condition `a[0][:i + 1] == s[:i + 1]` is met for the first time, otherwise `t` remains 1.
    print(s, sep='')
    #This is printed: s (where s is a prefix of a[0] up to the point where a[0][:x + 1] == s[:x + 1] for the first time)
    print(t)
    #This is printed: 1
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t`, an integer `n`, and two binary strings `a_{1}` and `a_{2}`. For each test case, it finds the longest common prefix between the first `x+1` characters of `a_{1}` and the entire string `a_{2}`, where `x` is the position just before the first mismatch. If no such prefix exists, `t` remains 1. The function then prints the found prefix and the value of `t`, which is always 1.

