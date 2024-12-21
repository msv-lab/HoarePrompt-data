#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and \( 10^9 \); `a` is in the range from 0 to `n // 1234567`; `b` is calculated based on the last valid `a` as `0` to `(n - a * 1234567) // 123456`; `c` is calculated from `n - a * 1234567 - b * 123456` resulting in a non-negative integer. At the end of the loop's execution, if no valid combination satisfies the equation, `b` may be at its maximum, and `c` would be the corresponding maximum calculated value.
    print('NO')
#Overall this is what the function does:The function receives an integer input `n` where \( 1 \leq n \leq 10^9 \), and checks if it is possible to express `n` as a combination of non-negative integer multiples of 1234567, 123456, and 1234. If such a combination exists, it prints 'YES' and exits. If no valid combination is found after exhausting all possibilities, it prints 'NO'. The function does not return any value and does not take any parameters. Edge cases include scenarios where `n` is less than the smallest multiple (i.e., less than 1234), and situations where `n` can only be expressed using a single type of multiple. The logic indeed lacks any handling for invalid input or verification of the input's range upon receipt.

