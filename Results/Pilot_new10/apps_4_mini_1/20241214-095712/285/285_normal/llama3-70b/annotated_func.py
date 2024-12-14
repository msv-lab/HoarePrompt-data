#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is the maximum number of times it can contribute to the sum without exceeding `n`, `b` is the maximum number of times it can contribute after considering the contributions of `a`, and `c` is the maximum number of times it can contribute after considering the contributions of both `a` and `b`, with  `a * 1234567 + b * 123456 + c * 1234` either equal to or less than `n`. If there is no combination of `a`, `b`, and `c` that satisfies the equation, then no output will be printed and the loop will finish without executing the print statement.
    print('NO')
#Overall this is what the function does:The function accepts no parameters and prompts the user to input a positive integer `n` (where 1 <= n <= 10^9). It attempts to find non-negative integers `a`, `b`, and `c` such that the equation `a * 1234567 + b * 123456 + c * 1234 = n` holds true. If such integers exist, it prints 'YES' and exits the function. If no valid combination is found after exhausting all possibilities, it prints 'NO'.

