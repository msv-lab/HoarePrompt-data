#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and n is an integer such that 1 <= n <= 50 for each test case.
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
        
    #State: `t` is an integer such that 1 <= t <= 50, and `n` is an integer such that 1 <= n <= 50 for each test case. The value of `t` remains unchanged, and the value of `n` is the last input integer provided during the loop execution.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 50`, and then for each of the `t` test cases, it reads another integer `n` from the input, where `1 <= n <= 50`. For each `n`, if `n` is odd, it prints 'NO'. If `n` is even and the length of the string `'AAB' * (n // 2)` is less than 200, it prints 'YES' followed by the string. If the length of the string is 200 or more, it prints 'NO'. After processing all test cases, the value of `t` remains unchanged, and `n` is the last input integer provided during the loop execution.

