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
        
    #State: t must be greater than 0 and less than or equal to 0, `n` is an input integer, and `s` is either '110' repeated `n // 2` times (if `n % 2` is not true) or remains unchanged from the precondition.
#Overall this is what the function does:The function processes multiple test cases, each involving an integer \( n \). For each \( n \), it checks if \( n \) is even. If \( n \) is even, it constructs a string consisting of '110' repeated \( n/2 \) times. If the length of this string is less than 200, it prints 'YES' followed by the constructed string; otherwise, it prints 'NO'. If \( n \) is odd, it directly prints 'NO'. The function implicitly accepts two integers \( t \) and \( n \) through user input, where \( 1 \leq t \leq 50 \) and \( 1 \leq n \leq 50 \), and it does not return any value explicitly but prints the results for each test case.

