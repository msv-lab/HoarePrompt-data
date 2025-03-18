#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50.
def func():
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n == 1:
            print('NO')
        else:
            ans = ''
            x = 0
            if n % 2 == 0:
                for j in range(n // 2):
                    ans += s[x] * 2
                    x += 1
            else:
                ans, x = 'AAA', 1
                for j in range(n // 2 - 1):
                    ans += s[x] * 2
                    x += 1
            print('YES')
            print(ans)
        
    #State: Output State: t is the number of test cases, for each test case: n is the input integer, if n is even, ans is a string consisting of pairs of characters from the string s repeated n/2 times, if n is odd, ans is 'AAA' followed by pairs of characters from s repeated (n-3)/2 times, and the output always includes 'YES' before printing ans.
#Overall this is what the function does:The function processes a series of test cases, each containing two integers \( t \) and \( n \). It prints 'YES' followed by a string \( ans \) based on the value of \( n \). If \( n \) is 1, it prints 'NO'. For even \( n \), \( ans \) consists of pairs of characters from the string \( s \) repeated \( n/2 \) times. For odd \( n \), \( ans \) starts with 'AAA' followed by pairs of characters from \( s \) repeated \( (n-3)/2 \) times. The function does not return any value but outputs the results for each test case.

