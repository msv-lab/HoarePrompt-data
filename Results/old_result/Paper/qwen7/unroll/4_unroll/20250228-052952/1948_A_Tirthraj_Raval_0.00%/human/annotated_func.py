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
        
    #State: Output State: t test cases are executed. For each test case, if the input integer n is odd, 'NO' is printed. If n is even, 'YES' is printed followed by a pattern consisting of alternating 'A' and 'B' characters repeated n//2 times.
#Overall this is what the function does:The function processes up to 50 test cases. For each test case, it reads an integer n (1 ≤ n ≤ 50). If n is odd, it prints 'NO'. If n is even, it prints 'YES' followed by a string of alternating 'A' and 'B' characters repeated n//2 times. After processing all test cases, it ends without returning any value.

