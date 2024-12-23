#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is at most `n // 1234567`, `b` is at most `(n - a * 1234567) // 123456`, `c` is a non-negative integer determined by the loop conditions, and if the loop executes completely without finding a valid combination, `n` is not expressible in the form `a * 1234567 + b * 123456 + c * 1234` for any non-negative integers.
    print('NO')
#Overall this is what the function does:The function reads a positive integer `n` from user input and attempts to determine if it can be expressed as a linear combination of the specific values 1234567, 123456, and 1234 using non-negative integer coefficients. It iterates over possible values for these coefficients (denoted as `a`, `b`, and `c`) and checks if such a combination exists. If a valid combination is found, it prints 'YES' and exits the function. If the function iterates through all possible combinations without finding a match, it prints 'NO'. The function does not return any value; its result is indicated solely through printed output. Therefore, the key postconditions are that if 'YES' is printed, `n` can be represented in the specified form; otherwise, if 'NO' is printed, `n` cannot be represented as such. Edge cases include the minimal possible value for `n` (which is 1) and larger values up to 10^9, where the performance of the loops must be considered.

