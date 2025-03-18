#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and n is an integer such that 1 <= n <= 50 for each test case.
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
        
    #State: t is an input integer such that 1 <= t <= 50, and n is an integer such that 1 <= n <= 50 for each test case. The loop has printed 'NO' for each odd n and 'YES' followed by a pattern of alternating 'A' and 'B' for each even n.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 50`. It then processes `t` test cases. For each test case, it reads an integer `n` from the input, where `1 <= n <= 50`. If `n` is odd, the function prints 'NO'. If `n` is even, the function prints 'YES', followed by a string pattern of alternating 'A' and 'B' characters of length `n`. After processing all test cases, the function has printed 'NO' for each odd `n` and 'YES' followed by the alternating pattern for each even `n`.

