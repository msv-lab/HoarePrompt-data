#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50, and the ticket number is a positive integer represented as a string of length exactly n containing only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 50, and `digits` is a map object containing integers from the input. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer between 2 and 50, and `digits` is a map object containing integers from the input. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (between 2 and 50) and reads a ticket number represented as a string of digits (either 4 or 7) of length `n`. It checks if the sum of the first half of the digits equals the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not handle invalid inputs or ensure that the digits are only 4 and 7, which could lead to unexpected behavior if the input does not meet these criteria.

