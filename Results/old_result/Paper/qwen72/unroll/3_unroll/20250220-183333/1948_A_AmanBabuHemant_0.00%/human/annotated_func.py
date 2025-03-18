#State of the program right berfore the function call: The function should be called with a single argument, which is a list of integers t, where each integer in the list satisfies 1 <= t[i] <= 50, and the length of the list is also within the range 1 <= len(t) <= 50. Each integer n in the list t represents a test case and must satisfy 1 <= n <= 50.
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
        
    #State: The loop has finished executing all iterations. For each integer `n` in the input list `t`, if `n` is odd, 'NO' was printed. If `n` is even and less than or equal to 200, 'YES' and a string `s` consisting of '110' repeated `n // 2` times was printed. If `n` is even and greater than 200, 'NO' was printed. The variable `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the user, representing the number of test cases. For each test case, it reads another integer `n` from the user. If `n` is odd, it prints 'NO'. If `n` is even and the length of the string '110' repeated `n // 2` times is less than 200, it prints 'YES' followed by the string. If `n` is even and the length of the string is 200 or more, it prints 'NO'. The function does not return any value.

