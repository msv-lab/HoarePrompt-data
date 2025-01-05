#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer with exactly n digits, which contains only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is a specific even integer such that 2 ≤ `n` ≤ 50, and `digits` is an iterable of integers from user input; if the sum of the first half of `digits` (up to `n / 2`) equals the sum of the second half (from `n / 2 + n % 2` onward), 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is an iterable of integers from user input; if the sum of the first half of `digits` (up to `n / 2`) equals the sum of the second half (from `n / 2 + n % 2` onward), 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 50) and expects user input for a ticket number that is a positive integer with exactly `n` digits composed solely of the digits 4 and 7. It calculates the sum of the first half of the digits and compares it to the sum of the second half, printing 'YES' if the two sums are equal and 'NO' otherwise. However, the function does not validate that the input digits are exclusively 4s and 7s, which could lead to incorrect results if other digits are present.

