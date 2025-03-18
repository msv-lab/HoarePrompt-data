#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^9, `a` is at most `(n // 1234567)`, `b` is at most `(n - a * 1234567) // 123456`, and `c` is non-negative such that `c = (n - a * 1234567 - b * 123456) // 1234`. If there exists any combination of `a`, `b`, and `c` such that `a * 1234567 + b * 123456 + c * 1234 == n`, 'YES' is printed and the program terminates. If no such combination is found after all iterations, the program completes without printing 'YES'.
    print('NO')
#Overall this is what the function does:The function does not accept any parameters and reads a positive integer `n` from user input. It checks if it is possible to express `n` as a sum of non-negative multiples of `1234567`, `123456`, and `1234`. If such a combination exists, it prints 'YES' and exits; otherwise, it prints 'NO' after all combinations have been checked.

