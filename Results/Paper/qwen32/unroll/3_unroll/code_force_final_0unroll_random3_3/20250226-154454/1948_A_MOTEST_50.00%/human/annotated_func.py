#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, there is an integer n such that 1 <= n <= 50.
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
        
    #State: - After all iterations, the variables `t` and `s` remain unchanged.
    #   - The variable `i` will be equal to `t` after the loop ends, as it increments from 0 to `t-1`.
    #   - The variables `n`, `ans`, and `x` will hold the values from the last iteration of the loop.
    #
    #Since the problem asks for the output state after all executions of the loop and not the printed output, we focus on the state of the variables:
    #
    #- `t` remains the same.
    #- `s` remains the same.
    #- `i` will be equal to `t` after the loop ends.
    #- `n`, `ans`, and `x` will hold the values from the last iteration of the loop.
    #
    #Thus, the output state can be described as:
    #
    #Output State:
#Overall this is what the function does:The function processes `t` test cases, each with an integer `n`. For each test case, it prints 'NO' if `n` is 1. Otherwise, it constructs a string of length `n` using uppercase letters from the alphabet and prints 'YES' followed by the constructed string. The string is formed by repeating each letter twice, with an extra 'AAA' if `n` is odd. The function does not modify the input values `t` and `n` beyond using them to determine the output.

