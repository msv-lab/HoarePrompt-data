#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each of the t test cases, n is an integer such that 1 ≤ n ≤ 50.
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
        
    #State: A series of 'YES' or 'NO' outputs, with 'YES' followed by a constructed string 'AAB' repeated `n // 2` times for each even `n`, and 'NO' for each odd `n`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `n`. It then prints 'YES' followed by a string consisting of 'AAB' repeated `n // 2` times if `n` is even and less than or equal to 100 characters long; otherwise, it prints 'NO'.

