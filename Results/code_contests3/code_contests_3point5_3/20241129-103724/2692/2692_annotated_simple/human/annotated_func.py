#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50. The ticket number is an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50, the ticket number is an integer of length n, digits is a list of integers obtained by mapping the int function to the input string after stripping any leading or trailing whitespaces. If the sum of the first half of the digits in the ticket number is equal to the sum of the second half of the digits in the ticket number, the program continues execution as normal. If not, the program prints 'NO'.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50, the ticket number is an integer of length n, digits is a list of integers obtained by mapping the int function to the input string after stripping any leading or trailing whitespaces. If the sum of the first half of the digits in the ticket number is equal to the sum of the second half of the digits in the ticket number, the program continues execution as normal. If the sums are not equal, the program prints 'NO'.
#Overall this is what the function does:The function `func` reads an even integer `n` and a ticket number with `n` digits. It then checks if the sum of the first half of the digits is equal to the sum of the second half. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not explicitly return any value, and the state after execution continues based on the sum comparison result.

