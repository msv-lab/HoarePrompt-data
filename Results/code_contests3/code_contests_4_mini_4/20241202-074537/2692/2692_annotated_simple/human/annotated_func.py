#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer with exactly n digits, which contains only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is a list of integers. If the sum of the first half of `digits` is equal to the sum of the second half, 'YES' is printed. Otherwise, if the sums are not equal, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is a list of integers containing exactly `n` digits, which are either 4 or 7. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function reads an even integer `n` (where 2 ≤ n ≤ 50) and a sequence of `n` digits (which must be either 4 or 7). It checks if the sum of the first half of the digits equals the sum of the second half. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not accept parameters and relies on user input for `n` and the digits.

