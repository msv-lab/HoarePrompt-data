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
        
    #State: After all iterations of the loop, `t` must be greater than 0 and less than or equal to 0, `n` is an input integer, and `s` is a string consisting of 'AAB' repeated `n // 2` times.
#Overall this is what the function does:The function processes multiple test cases where for each test case, it reads an integer \( t \) and then \( t \) integers \( n \). For each \( n \), it checks if \( n \) is odd or even. If \( n \) is odd, it prints 'NO'. If \( n \) is even, it constructs a string \( s \) consisting of 'AAB' repeated \( n/2 \) times. If the length of \( s \) is less than 200, it prints 'YES' followed by \( s \); otherwise, it prints 'NO'. The function does not return any value but prints the results for each test case.

