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
        
    #State: Output State: After executing the loop for `t` iterations, for each `n`, if `n` is odd, the output will be 'NO'. If `n` is even, the output will be 'YES' followed by a pattern consisting of alternating 'A' and 'B' characters repeated `n//2` times.
#Overall this is what the function does:The function reads a positive integer `t` representing the number of test cases. For each test case, it reads another positive integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' followed by a pattern consisting of alternating 'A' and 'B' characters repeated `n//2` times. The function does not return any value.

