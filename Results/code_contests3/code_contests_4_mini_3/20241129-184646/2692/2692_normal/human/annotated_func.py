#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a string of digits with length exactly n that contains only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50; `digits` is an iterable of integers representing the digits of the ticket number, which are either 4 or 7. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is an iterable of integers representing the digits of the ticket number, which are either 4 or 7. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 50) and reads a string of digits from input, which must be exactly `n` characters long and consist of the digits '4' and '7'. It checks if the sum of the first half of the digits equals the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. However, the function does not return any values, as it only prints the result to the console. Additionally, it assumes that the input is valid and does not handle cases where the input does not meet the specified conditions.

