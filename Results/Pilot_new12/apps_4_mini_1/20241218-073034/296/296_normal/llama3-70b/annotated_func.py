#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func():
    n = int(input())
    if (n == 2) :
        print('NO')
    else :
        print('YES')
        k = 2
        print(k)
        print('1', n // 2)
        print('1', n)
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9. If `n` is equal to 2, the output is 'NO'. If `n` is greater than 2, the output is '1' followed by `n`, and `k` is set to 2.
#Overall this is what the function does:The function reads a positive integer `n` (where 2 <= n <= 10^9) from user input. If `n` is equal to 2, it outputs 'NO'. If `n` is greater than 2, it outputs 'YES', followed by the integer '2', and then outputs '1' followed by `n // 2` and '1' followed by `n`. There are no return values, as the function solely prints output based on the condition of `n`. It does not handle any other cases, such as when `n` is less than 2, which may lead to undefined behavior since inputs are expected to fall within the provided range.

