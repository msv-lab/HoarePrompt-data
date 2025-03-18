#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5, and for each trace a, there exists a suitable string s.
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
        
    #State: The loop has completed all iterations. For each test case, the variable `r` is a string constructed from characters in `a` based on the indices provided in `s`, and each character in `r` is the character in `a` at the position specified by the corresponding value in `s` (0-based index), with the character being incremented by 1 each time it is used. The variables `t`, `n`, and `a` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of integers `s`. It then constructs a string `r` by mapping each integer in `s` to a character in the alphabet string `a` (where `a` is 'abcdefghijklmnopqrstuvwxyz'). Each character in `r` is determined by the index of the corresponding integer in `s` within the list `b`, which is initialized to `[0] * 26`. The character is incremented by 1 each time it is used. The function prints the constructed string `r` for each test case. The variables `t`, `n`, and `a` remain unchanged after the function execution.

