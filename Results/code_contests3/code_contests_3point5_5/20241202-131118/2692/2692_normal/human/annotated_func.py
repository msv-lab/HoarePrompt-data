#State of the program right berfore the function call: n is a positive even integer and the ticket number is a positive integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is a positive even integer, ticket number is a positive integer of length n, digits is a map object containing integer values of the input after stripping whitespaces. If the sum of the first half of the digits is equal to the sum of the second half of the digits, then the program continues execution. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *n is a positive even integer and the ticket number is a positive integer of length n. If the sum of the first half of the digits of the ticket number is equal to the sum of the second half of the digits, then the program continues execution. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function does not accept any parameters. It reads an integer `n` representing the length of a ticket number and a sequence of integers as the ticket number. It then checks if the sum of the first half of the digits of the ticket number is equal to the sum of the second half of the digits. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'.

