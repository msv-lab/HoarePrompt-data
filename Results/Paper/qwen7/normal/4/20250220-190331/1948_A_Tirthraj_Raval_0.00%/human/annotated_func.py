#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50.
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
        
    #State: `t` is 0, `n` is an integer between 1 and 50 (inclusive), and `pattern` is either an empty list or contains a sequence of characters 'A' and 'B' as described by the loop's behavior.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and checks if `n` is odd or even. If `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' and then generates a pattern consisting of alternating 'A' and 'B' characters of length `n`. The function does not return any value but prints the results for each test case.

