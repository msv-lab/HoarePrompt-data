#State of the program right berfore the function call: n is a positive integer between 1 and 10^9 (inclusive), representing Kolya's initial game-coin score.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `a` is `n // 1234567`, `b` is `(n - a * 1234567) // 123456`, and `c` is `(n - a * 1234567 - b * 123456) // 1234` if the loop executes; otherwise, `a`, `b`, and `c` are undefined.
    print('NO')
#Overall this is what the function does:The function takes an integer input from the user, checks if the number can be represented as a sum of multiples of 1234567, 123456, and 1234, and prints 'YES' if such a representation exists, or 'NO' otherwise. The function does not return any value, it only prints the result to the console. The input integer is expected to be a positive integer between 1 and 10^9 (inclusive). If the input is outside of this range, the function may not behave as expected. The function's execution terminates when it finds a valid representation or exhausts all possible combinations, at which point it prints the result and terminates.

