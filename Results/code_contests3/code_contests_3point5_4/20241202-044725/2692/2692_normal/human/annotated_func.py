#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50. The ticket number is an integer with exactly n digits.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer between 2 and 50, ticket number is an integer with exactly n digits. If the sum of the first half of the digits of the ticket number is equal to the sum of the second half of the digits of the ticket number, the program continues. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *n is an even integer between 2 and 50, the ticket number is an integer with exactly n digits. If the sum of the first half of the digits of the ticket number is equal to the sum of the second half of the digits of the ticket number, the program continues. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an even integer `n` between 2 and 50 as the number of digits in a ticket number. The function then reads the ticket number digits and checks if the sum of the first half of the digits is equal to the sum of the second half. If the sums are equal, it prints 'YES', otherwise it prints 'NO'. This function specifically handles ticket numbers with `n` digits where `n` is an even integer between 2 and 50.

