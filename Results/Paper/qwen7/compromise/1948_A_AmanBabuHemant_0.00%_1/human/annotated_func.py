#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = '110' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: Output State: `t` test cases are processed. For each test case:
    #- If the given integer `n` is odd, the output is 'NO'.
    #- If the given integer `n` is even and less than 400, the output is 'YES' followed by a string consisting of '110' repeated `n//2` times, but truncated to 200 characters if necessary.
    #- If the given integer `n` is even but greater than or equal to 400, the output is 'NO'.
#Overall this is what the function does:The function processes up to 50 test cases, each involving an integer `n`. For each test case, if `n` is odd, it outputs 'NO'. If `n` is even and less than 400, it outputs 'YES' followed by a string consisting of '110' repeated `n//2` times, truncated to 200 characters if necessary. If `n` is even and 400 or greater, it outputs 'NO'. The function does not return any value but prints the results directly.

