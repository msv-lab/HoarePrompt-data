#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is at most `n // 1234567`, `b` is at most `(n - a * 1234567) // 123456`, `c` is a non-negative integer determined by `(n - a * 1234567 - b * 123456) // 1234` such that the equation `a * 1234567 + b * 123456 + c * 1234` equals `n` is satisfied. If no combination of non-negative integers `a`, `b`, and `c` exists such that the equation holds, the program will not print 'YES' and will terminate after evaluating all possible values of `a` and `b`.
    print('NO')
#Overall this is what the function does:The function accepts an integer input `n` and checks if it can be expressed as a linear combination of the integers 1234567, 123456, and 1234 using non-negative coefficients. If such a combination exists, it prints 'YES'; otherwise, it prints 'NO'.

