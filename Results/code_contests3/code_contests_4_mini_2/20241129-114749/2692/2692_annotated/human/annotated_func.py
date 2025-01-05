#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and ticket_number is a string of digits with length exactly n that consists only of the digits 0 to 9.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50 and `digits` is a list of integers. If the sum of the first half of the `digits` list equals the sum of the second half, 'YES' is printed. Otherwise, if the sums are not equal, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `ticket_number` is a string of digits with length exactly `n` consisting only of the digits 0 to 9. If the sum of the first half of the digits (converted from `ticket_number`) equals the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function reads an even integer `n` (where 2 ≤ n ≤ 50) and a string of digits (ticket_number) of length exactly `n`. It checks whether the sum of the first half of the digits equals the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value; it only prints the result based on the comparison of the sums. Additionally, the input handling assumes that the input is valid and does not account for any invalid input cases.

