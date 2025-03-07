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
        
    #State: Output State: t is the number of test cases initially given, each test case processes an integer n between 1 and 50. For each n:
    #- If n is odd, prints "NO".
    #- If n is even and less than 400, prints "YES" followed by a string 'AAB' repeated (n//2) times, but the string length does not exceed 200 characters. If n is even but the resulting string would be 200 or more characters long, prints "NO".
#Overall this is what the function does:The function processes multiple test cases, each involving an integer \( n \) (where \( 1 \leq n \leq 50 \)). For each \( n \), it checks if \( n \) is odd or even. If \( n \) is odd, it prints "NO". If \( n \) is even, it constructs a string consisting of 'AAB' repeated \( \frac{n}{2} \) times. If the constructed string length is less than 200 characters, it prints "YES" followed by the string; otherwise, it prints "NO". The function does not return any value but outputs the results for each test case.

