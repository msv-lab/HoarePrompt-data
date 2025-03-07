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
        
    #State: After the loop executes all the iterations, `t` will be 0, indicating that all iterations are completed. The value of `n` will be the integer from the last iteration's input. If `n` from the last iteration is odd, no string `s` is generated. If `n` from the last iteration is even, `s` will be the string `'AAB'` repeated `n // 2` times, provided its length is less than 200. If the length of `s` is 200 or more, no string `s` is printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it constructs a string `s` by repeating the substring 'AAB' `n // 2` times and prints 'YES' followed by the string `s` if the length of `s` is less than 200. If the length of `s` is 200 or more, it prints 'NO'.

