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
        
    #State: For each input integer `n` (1 ≤ n ≤ 50) within the range specified by `t`, if `n` is odd, the output will be 'NO'. If `n` is even, the output will be 'YES' followed by a pattern consisting of alternating 'A' and 'B' characters, with the length of the pattern being `n/2`.
#Overall this is what the function does:The function processes a series of test cases (up to 50) where for each case, it reads an integer \( n \) (between 1 and 50). If \( n \) is odd, it outputs 'NO'. If \( n \) is even, it outputs 'YES' followed by a string of alternating 'A' and 'B' characters, with the length of the string being \( n/2 \). After processing all test cases, no variables are returned, but the console will display the appropriate output for each case.

