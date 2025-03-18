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
        
    #State: After all iterations of the loop have finished, `t` must be greater than 2, `n` is an input integer, and `n` must be greater than 12. The variable `pattern` will be a string consisting of alternating 'A' and 'B' characters with a length of `n // 2`.
#Overall this is what the function does:The function processes a series of test cases (up to 50) where for each test case, it reads an integer \( n \) (between 1 and 50). If \( n \) is odd, it prints 'NO'. Otherwise, it prints 'YES' and generates a string of alternating 'A' and 'B' characters of length \( n/2 \), then prints this string. After processing all test cases, the function does not return any value.

