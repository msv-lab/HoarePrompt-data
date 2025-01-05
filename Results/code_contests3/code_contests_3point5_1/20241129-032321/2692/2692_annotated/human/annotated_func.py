#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50. The ticket number is an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50, digits is a list of integers obtained from the input ticket number. If the sum of the first half of digits is equal to the sum of the second half of digits, then the program continues. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50 and the ticket number is an integer of length n. Digits is a list of integers obtained from the input ticket number. If the sum of the first half of digits is equal to the sum of the second half of digits, then the program continues. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function does not accept any parameters. It reads an even integer `n` representing the length of a ticket number and a list of integers `digits` representing the ticket number. It then checks if the sum of the first half of digits is equal to the sum of the second half of digits. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'. The program assumes the ticket number has a valid length of `n` and does not handle cases where `n` is odd or outside the range of 2 to 50.

