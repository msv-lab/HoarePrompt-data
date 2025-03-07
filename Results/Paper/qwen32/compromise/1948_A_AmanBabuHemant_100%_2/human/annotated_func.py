#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
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
        
    #State: After the loop executes all the iterations, the value of `t` remains unchanged, and `n` holds the value of the last integer input within the loop. The program will have printed 'YES' or 'NO' for each iteration based on whether the input `n` is even and less than or equal to 100, and if 'YES', it will have printed a string of 'AAB' repeated `n // 2` times.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n`. For each test case, it determines if `n` is even and less than or equal to 100. If both conditions are met, it outputs 'YES' followed by a string of 'AAB' repeated `n // 2` times. If `n` is odd or greater than 100, it outputs 'NO'.

