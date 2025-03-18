#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each test case, n is an integer such that 1 <= n <= 50.
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
        
    #State: `t` is the same as the initial input integer; `n` is the integer input in the last iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. It then checks if `n` is even and less than or equal to 100. If so, it outputs 'YES' followed by a string of 'AAB' repeated `n // 2` times. If `n` is odd or the resulting string would be longer than 200 characters, it outputs 'NO'.

