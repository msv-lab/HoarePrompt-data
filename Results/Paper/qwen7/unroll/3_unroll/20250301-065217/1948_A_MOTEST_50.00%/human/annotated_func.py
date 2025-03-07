#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
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
        
    #State: The console will display "NO" for each input value of `t` where the input value is 1, and "YES" followed by a string `ans` constructed based on the input value `n`. The string `ans` will be composed of characters from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' according to the rules defined in the loop. Each iteration of the outer loop (`for i in range(t)`) will reset the variables `n`, `ans`, and `x` to their initial states.
#Overall this is what the function does:The function processes a series of test cases (up to 50) where for each case, it takes an integer `n` (1 ≤ n ≤ 50). If `n` is 1, it prints "NO". Otherwise, it constructs a string `ans` using characters from 'A' to 'Z' based on the value of `n` and prints "YES" followed by `ans`. After processing all test cases, the function does not return any value but modifies the console output accordingly.

