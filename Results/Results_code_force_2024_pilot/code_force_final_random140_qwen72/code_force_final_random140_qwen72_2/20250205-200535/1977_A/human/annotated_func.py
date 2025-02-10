#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. Each test case consists of two integers n and m where 1 ≤ n, m ≤ 100, representing the number of moves and the desired number of cubes in the tower, respectively.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: After all iterations of the loop have executed, `t` is an integer where 1 ≤ t ≤ 100, and the loop has processed `t` test cases. For each test case, the values of `n` and `m` were read from the input, and the loop printed 'NO' if `n` was less than `m`, or 'YES' if `n` and `m` were both odd or both even. The loop has completed all its iterations, and no further test cases are left to process.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `m`. For each test case, it reads `n` and `m` from the input. If `n` is less than `m`, it prints 'NO'. Otherwise, it prints 'YES' if both `n` and `m` are either both odd or both even. After processing all test cases, the function completes and no further test cases are left to process.

