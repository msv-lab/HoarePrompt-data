#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, there is an integer n such that 1 <= n <= 50.
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
        
    #State: a series of 'YES' or 'NO' for each test case, with 'YES' followed by a pattern of 'AB' repeated `n // 2` times for even `n`.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n`. For each test case, it outputs 'NO' if `n` is odd, and 'YES' followed by a pattern of alternating 'A' and 'B' characters repeated `n // 2` times if `n` is even.

