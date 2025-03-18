#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each test case, n is an integer such that 1 <= n <= 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: `t` is an input integer such that `t` is 0; `n` is the last input integer. If `n` is odd, then no additional changes are made to the variables. If `n` is even, then `pattern` is a list with `n` elements alternating between 'A' and 'B', starting with 'A'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' followed by a string of length `n` consisting of alternating 'A' and 'B' characters, starting with 'A'.

