#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer with exactly n digits, which consists only of the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ n ≤ 50; `digits` is a map object representing a list of integers from input. If the sum of the first half of `digits` is equal to the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ n ≤ 50, and `digits` is a map object representing a list of integers from input. If the sum of the first half of `digits` is equal to the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 50) and reads a ticket number consisting of exactly `n` digits, which are expected to be either 4 or 7. It checks if the sum of the first half of the digits is equal to the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not validate that the digits are strictly 4 or 7, which is a potential edge case.

