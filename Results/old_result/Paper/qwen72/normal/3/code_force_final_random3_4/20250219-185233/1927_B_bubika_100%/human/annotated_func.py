#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but it should internally handle multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2 ⋅ 10^5) representing the length of the lost string, and a list of integers `a` of length `n` (0 ≤ a_i < n) representing the trace of the string. The sum of `n` over all test cases does not exceed 2 ⋅ 10^5. It is guaranteed that for each trace, there exists at least one valid string `s` consisting of lowercase Latin letters a-z.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: The variable `a` remains 'abcdefghijklmnopqrstuvwxyz', `t` is the number of test cases minus 1, `b` is a list of 26 integers where each integer at index `x` (for each `x` in `s` across all test cases) is incremented by the number of times that `x` appears in `s`, `n` is the last input integer greater than 0, `s` is the last list of integers input by the user, `r` is the last string containing the characters from `a` at the indices specified by `s` in the order they appear in `s`.
#Overall this is what the function does:The function `func` handles multiple test cases internally. Each test case involves an integer `n` and a list of integers `s` of length `n`. The function constructs and prints a string `r` for each test case, where each character in `r` is determined by the corresponding integer in `s` and a fixed alphabet string `a` ('abcdefghijklmnopqrstuvwxyz'). The function does not return any value; it only prints the constructed strings. After the function concludes, the variable `a` remains unchanged, `t` is the number of test cases minus 1, `b` is a list of 26 integers reflecting the frequency of each index in `s` across all test cases, `n` is the last input integer greater than 0, and `s` is the last list of integers input by the user.

