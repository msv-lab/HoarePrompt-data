#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
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
        
    #State: t equals 0, there exists at least one value of n that is an even integer and at least 2, and for each such n, the variable pattern is a string consisting of alternating 'A' and 'B' characters.
#Overall this is what the function does:The function processes a series of test cases (up to 50). For each test case, it reads an integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' and then generates a string of length `n` consisting of alternating 'A' and 'B' characters, which it also prints. After processing all test cases, the function ends.

