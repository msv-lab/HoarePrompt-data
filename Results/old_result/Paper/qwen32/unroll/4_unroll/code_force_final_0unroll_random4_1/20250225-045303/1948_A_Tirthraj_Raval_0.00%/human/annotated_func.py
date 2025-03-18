#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 1 <= n <= 50.
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
        
    #State: For each of the `t` test cases, the output is either "NO" if `n` is odd, or "YES" followed by a pattern of alternating 'A's and 'B's of length `n` if `n` is even.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it outputs "NO". If `n` is even, it outputs "YES" followed by a string of alternating 'A's and 'B's of length `n`.

