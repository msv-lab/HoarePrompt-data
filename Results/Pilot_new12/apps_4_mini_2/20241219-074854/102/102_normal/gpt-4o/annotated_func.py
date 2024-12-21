#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10,000,000.
def func_1():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            print('YES')
            print(x, y)
            return
        
    #State of the program after the  for loop has been executed: `a` is an integer such that 1 ≤ `a` ≤ 10,000,000, `b` is an integer, `n` is a non-negative integer. The loop exhaustively checks all values of `x` from 0 to `n // a`. If `n - x * a` is divisible by `b`, then the program finds `y` as `(n - x * a) // b` and prints 'YES', along with the values of `x` and `y`. If no such `x` satisfies the condition for all iterations, then no values are printed, and the loop completes its execution without a return.
    print('NO')
#Overall this is what the function does:The function `func_1` accepts no parameters and reads three integers `n`, `a`, and `b` from user input. It then attempts to determine if there exist non-negative integers `x` and `y` such that the equation `n = x * a + y * b` holds true, where `x` can range from `0` to `n // a`. If such a pair `(x, y)` is found, it prints 'YES' followed by the values of `x` and `y`. If no such pair is found after exhaustively checking all possible values of `x`, the function prints 'NO'. The function does not return any values and will either print 'YES' with the respective values or 'NO', completing its execution with no values being returned or stored. Potential edge cases include scenarios where no valid (x, y) pairs exist, resulting in only the 'NO' message being printed. Additionally, the function assumes valid integer inputs within the specified range but does not handle any invalid inputs or exceptions that could arise.

