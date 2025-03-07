#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = 'AAB' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: Output State: t input integers between 1 and 50, inclusive, each followed by either 'NO', 'YES' and the string 'AAB' * (n // 2) if the length of the string is less than 200, or just 'NO'.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads an integer `n`. If `n` is odd, it outputs 'NO'. If `n` is even and the string 'AAB' repeated `n//2` times is less than 200 characters long, it outputs 'YES' followed by the string. Otherwise, it outputs 'NO'. After processing all test cases, it outputs `t` lines, each containing either 'NO' or 'YES' and possibly a string of 'AAB' repeated `n//2` times if the string length is less than 200.

