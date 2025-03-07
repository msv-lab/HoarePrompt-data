#State of the program right berfore the function call: The function should take an integer n as input, where 1 <= n <= 50, and return a string of uppercase Latin letters with exactly n special characters, or "NO" if no such string exists.
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
        
    #State: Output State: The function will print "NO" for any odd value of `n` and "YES" followed by a string of '110' repeated `n // 2` times for any even value of `n` where the length of the string is less than 200. If `n` is even but the length of the string is 200 or more, it will print "NO". The loop will execute `t` times, and the state of `t` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` from the input. If `n` is odd or if the length of the string formed by repeating '110' `n // 2` times is 200 or more, the function prints "NO". If `n` is even and the length of the string is less than 200, the function prints "YES" followed by the string. The function does not return any value; it only prints the results. The state of `t` remains unchanged after the function execution.

