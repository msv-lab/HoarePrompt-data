#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each test case, n is an integer such that 1 <= n <= 50.
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
        
    #State: the program will have printed 'NO' or 'YES' followed by a string of '110's for each input `n` depending on whether `n` is odd or even and if the constructed string's length is less than 200. The value of `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it constructs a string consisting of '110' repeated `n // 2` times and prints 'YES' followed by the string if the string's length is less than 200; otherwise, it prints 'NO'.

