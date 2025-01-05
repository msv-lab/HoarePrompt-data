#State of the program right berfore the function call: n is a positive even integer (2 <= n <= 50) and the ticket number is an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is a positive even integer between 2 and 50, ticket number is an integer of length n, digits is a list of integers extracted from the input ticket number. If the sum of the first half of digits is equal to the sum of the second half of digits, then the program executes the if part. Otherwise, the program executes the else part.
    #State of the program after the if block has been executed: *n is a positive even integer between 2 and 50, and the ticket number is an integer of length n. The digits list contains integers extracted from the input ticket number. If the sum of the first half of digits is equal to the sum of the second half of digits, then the program continues. Otherwise, the program terminates.
#Overall this is what the function does:The function `func` reads an input ticket number, extracts the digits, and checks if the sum of the first half of digits is equal to the sum of the second half. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not accept any parameters explicitly but relies on user input for the ticket number. It does not explicitly return any value but prints the validation result based on the comparison of digit sums.

