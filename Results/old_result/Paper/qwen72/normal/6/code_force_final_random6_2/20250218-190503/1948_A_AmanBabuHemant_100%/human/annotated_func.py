#State of the program right berfore the function call: The function should be called with a single integer t (1 ≤ t ≤ 50) as the number of test cases, and for each test case, a single integer n (1 ≤ n ≤ 50) is provided.
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
        
    #State: `t` is 0, and `n` is an integer between 1 and 50, inclusive, for each test case. If `n` is odd, no changes are made to `n`. If `n` is even, `s` is a string consisting of 'AAB' repeated `n // 2` times, and the length of `s` is `n // 2 * 3`. If `n // 2 * 3` is less than 200, the length of `s` remains less than 200. If `n // 2 * 3` is greater than or equal to 200, the length of `s` remains greater than or equal to 200.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 ≤ t ≤ 50) indicating the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 50). If `n` is odd, the function prints 'NO'. If `n` is even, it constructs a string `s` by repeating 'AAB' `n // 2` times. If the length of `s` is less than 200, the function prints 'YES' followed by the string `s`. If the length of `s` is 200 or more, the function prints 'NO'. After processing all test cases, the function does not return any value, but the final state of the program is that `t` test cases have been processed and the appropriate output has been printed for each.

